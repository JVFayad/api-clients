from django.shortcuts import render
from django.core.cache import cache

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

# TODO Mover essas funções
def retrieve_cache(key, queryset_method):
    if cache.get(key):
        queryset = cache.get(key)
    else:
        queryset = queryset_method()
        cache.set(key, queryset)

    return queryset

def update_cache(key, queryset_method):
    cache.delete(key)
    cache.set(key, queryset_method())


class ClientListCreate(generics.ListCreateAPIView):
    """
    List and Create Clients
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        """
        Get clients or retrieve data from cache 
        """
        queryset = retrieve_cache(
            'clients', super(ClientListCreate, self).get_queryset)
        
        return queryset

    def post(self, *args, **kwargs):
        """
        Create client and update data on cache 
        """
        _super = super(ClientListCreate, self)
        response = _super.post(*args, **kwargs)
        
        if response.status_code == 201:
            update_cache(
                'clients', _super.get_queryset)

        return response


class ClientRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update and Delete Clients
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        """
        Update client and update data on cache 
        """
        _super = super(ClientRetrieveUpdateDestroy, self)
        response = _super.put(request, *args, **kwargs)

        if response.status_code == 200:
            update_cache(
                'clients', _super.get_queryset)

        return response

    def delete(self, request, *args, **kwargs):
        """
        Delete client and update data on cache 
        """
        _super = super(ClientRetrieveUpdateDestroy, self)
        response = _super.delete(request, *args, **kwargs)

        if response.status_code == 204:
            update_cache(
                'clients', _super.get_queryset)

        return response


class ClientProductList(APIView):
    """
    List and Add favorite products to Clients
    """
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

    def get_cache_key(self, client_id):
        """
        Returns Key for queryset cache
        """
        key = 'client_{}_favorite_products'.format(
            client_id
        )

        return key

    def get(self, *args, **kwargs):
        """
        Get favorite products from client 
        """
        client_id = kwargs.get('pk')

        try:
            client = Client.objects.get(id=kwargs.get('pk'))
        except Client.DoesNotExist:
            raise NotFound(detail="Client not found.")

        key = self.get_cache_key(client_id)

        favorite_products = retrieve_cache(
            key, client.favorite_products.all)

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
        key = self.get_cache_key(client_id)

        if not favorite_products.filter(id=product_id).exists():
            favorite_products.add(product)
            update_cache(key, favorite_products.all)

        return Response(
            self.serializer_class(product).data, 
            status=200
        )
    
