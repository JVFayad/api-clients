from django.shortcuts import render

from .models import Client
from .serializers import ClientSerializer

from products.models import Product
from products.serializers import ProductSerializer

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import NotFound, MethodNotAllowed
from rest_framework.permissions import IsAuthenticated


class ClientList(generics.ListCreateAPIView):
    """
    List and Create Clients
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated,)


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update and Delete Clients
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated,)


class ClientProductList(APIView):
    """
    List and Add favorite products to Clients
    """
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, *args, **kwargs):
        """
        List favorite products from client
        """
        client_id = kwargs.get('pk')

        try:
            client = Client.objects.get(id=kwargs.get('pk'))
        except Client.DoesNotExist:
            raise NotFound(detail="Client not found.")

        favorite_products = client.favorite_products.all()

        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(
            favorite_products, self.request, view=self)

        serializer = self.serializer_class(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)     

    def post(self, *args, **kwargs):
        """
        Add client favorite product
        """
        client_id = kwargs.get('pk')
        product_id = self.request.data.get('product_id')

        try:
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            raise NotFound(detail="Client not found.")
        else:
            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                raise NotFound(detail="Product not found.")

        favorite_products = client.favorite_products
        
        if not favorite_products.filter(id=product_id).exists():
            favorite_products.add(product)

        return Response(
            self.serializer_class(product).data, 
            status=200
        )
    
