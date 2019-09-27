from django.shortcuts import render

from .models import Client
from .serializers import ClientSerializer
from products.serializers import ProductSerializer

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.exceptions import APIException


class ClientList(generics.ListCreateAPIView):
    """
    List and Create Clients
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update and Delete Clients
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientProductList(APIView):
    """
    List and Add favorite products to Clients
    """
    serializer_class = ProductSerializer

    def get(self, *args, **kwargs):
        try:
            client = Client.objects.get(id=kwargs.get('pk'))
        except Client.DoesNotExist:
            raise APIException(detail="Not found.")

        favorite_products = client.favorite_products.all()

        paginator = LimitOffsetPagination()
        result_page = paginator.paginate_queryset(favorite_products, self.request, view=self)
        serializer = self.serializer_class(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)     

    def post(self, *args, **kwargs):
        return 0
    
