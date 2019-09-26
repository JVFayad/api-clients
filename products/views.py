from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework import generics


class ProductList(generics.ListAPIView):
    """
    List Products
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveAPIView):
    """
    Retrieve Products
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
