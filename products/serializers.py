from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer class for Products
    """
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'brand', 'image', 'reviewScore']