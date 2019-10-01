from django.test import TestCase
from django.test import Client as TestClient
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.cache import cache

from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from .models import Client
from .serializers import ClientSerializer
 

class GetAllClientsTest(APITestCase):
    """
     Test for GET clients 
    """
    def setUp(self):
         # Handling auth
        self.user = User.objects.create_superuser(
            'admin', 'admin@admin.com', 'admin123')
        
        self.token = Token.objects.create(user=self.user)
        self.client.force_login(user=self.user)

        Client.objects.create(
            name='Joao Client', email='joao@client.com')
        Client.objects.create(
            name='Pedro Client', email='pedro@client.com')

    def test_get_all_clients(self):
        response = self.client.get(
            reverse('create_list_clients'), 
            format='json', HTTP_AUTHORIZATION=self.token.key)

        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)

        # Handling manual cache
        cache.delete('clients');

        self.assertEqual(response.data.get('results'), serializer.data)
        self.assertEqual(response.status_code, 200)


class GetSingleClientTest(APITestCase):
    """
     Tests for GET single client
    """
    def setUp(self):
        # Handling auth
        self.user = User.objects.create_superuser(
            'admin', 'admin@admin.com', 'admin123')

        self.token = Token.objects.create(user=self.user)
        self.client.force_login(user=self.user)

        self.client1 = Client.objects.create(
            name='Joao Client', email='joao@client.com')

    def test_get_single_client(self):
        response = self.client.get(
            reverse(
                'detail_update_delete_clients', 
                kwargs={'pk': self.client1.id}),
            format='json', 
            HTTP_AUTHORIZATION=self.token.key)
            
        serializer = ClientSerializer(self.client1)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)

    def test_get_invalid_client(self):
        response = self.client.get(
            reverse(
                'detail_update_delete_clients', 
                kwargs={'pk': 999}),
            format='json', 
            HTTP_AUTHORIZATION=self.token.key)

        self.assertEqual(response.status_code, 404)


class CreateClientTest(APITestCase):
    """
    Tests for POST (create client)
    """
    def setUp(self):
        # Handling auth
        self.user = User.objects.create_superuser(
            'admin', 'admin@admin.com', 'admin123')

        self.token = Token.objects.create(user=self.user)
        self.client.force_login(user=self.user)

        self.client1_data = {
            'name': 'Maria Client',
            'email': 'maria@client.com'
        }

        self.client2_data = {
            'name': 'Ted Client',
            'email': '',
        }

    def test_create_client(self):
        response = self.client.post(
            reverse('create_list_clients'), data=self.client1_data,
            format='json', HTTP_AUTHORIZATION=self.token.key)

        # Handling manual cache
        cache.delete('clients');

        self.assertEqual(response.status_code, 201)

    def test_create_invalid_client(self):
        response = self.client.post(
            reverse('create_list_clients'), data=self.client2_data,
            format='json', HTTP_AUTHORIZATION=self.token.key)
            
        self.assertEqual(response.status_code, 400)


class UpdateClientTest(APITestCase):
    """
    Tests for PUT (update client)
    """
    def setUp(self):
        # Handling auth
        self.user = User.objects.create_superuser(
            'admin', 'admin@admin.com', 'admin123')

        self.token = Token.objects.create(user=self.user)
        self.client.force_login(user=self.user)

        self.client1 = Client.objects.create(
            name='Gustavo Client', email='gustavo@client.com')
        self.client2 = Client.objects.create(
            name='Jose Client', email='jose@client.com')

        self.client1_data = {
            'name': 'Gustavo Client',
            'email': 'gu@client.com'
        }

        self.client2_data = {
            'name': '',
            'email': 'ze@client.com',
        }

    def test_update_client(self):
        response = self.client.put(
            reverse(
                'detail_update_delete_clients', 
                kwargs={'pk': self.client1.id}), 
            data=self.client1_data,
            format='json', 
            HTTP_AUTHORIZATION=self.token.key)

        # Handling manual cache
        cache.delete('clients');

        self.assertEqual(response.status_code, 200)

    def test_update_invalid_client(self):
        response = self.client.put(
            reverse(
                'detail_update_delete_clients', 
                kwargs={'pk': self.client2.id}), 
            data=self.client2_data,
            format='json', 
            HTTP_AUTHORIZATION=self.token.key)
            
        self.assertEqual(response.status_code, 400)


class DeleteClientTest(APITestCase):
    """
    Tests for DELETE client
    """
    def setUp(self):
        # Handling auth
        self.user = User.objects.create_superuser(
            'admin', 'admin@admin.com', 'admin123')

        self.token = Token.objects.create(user=self.user)
        self.client.force_login(user=self.user)

        self.client1 = Client.objects.create(
            name='Gustavo Client', email='gustavo@client.com')
        self.client2 = Client.objects.create(
            name='Jose Client', email='jose@client.com')

    def test_delete_client(self):
        response = self.client.delete(
            reverse(
                'detail_update_delete_clients', 
                kwargs={'pk': self.client1.id}),
            format='json', 
            HTTP_AUTHORIZATION=self.token.key)

        # Handling manual cache
        cache.delete('clients');

        self.assertEqual(response.status_code, 204)

    def test_delete_invalid_client(self):
        response = self.client.put(
            reverse(
                'detail_update_delete_clients', 
                kwargs={'pk': 99}), 
            format='json', 
            HTTP_AUTHORIZATION=self.token.key)
            
        self.assertEqual(response.status_code, 404)
