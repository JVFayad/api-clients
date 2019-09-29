from django.shortcuts import render

from .models import Product
from .serializers import ProductSerializer

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class ProductList(generics.ListAPIView):
    """
    List Products
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)


class ProductDetail(generics.RetrieveAPIView):
    """
    Retrieve Products
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
