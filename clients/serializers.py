from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    """
    Serializer class for Clients
    """
    class Meta:
        model = Client
        fields = ['id', 'name', 'email']