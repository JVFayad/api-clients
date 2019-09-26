from django.shortcuts import render
from .models import Client
from .serializers import ClientSerializer
from rest_framework import generics


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
