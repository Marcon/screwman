from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from orders.models import Manufacturer

User = get_user_model()


class ManufacturersListTest(APITestCase):

    def setUp(self):
        self.url = reverse('manufacturers-list')

    @classmethod
    def setUpTestData(cls):
        User.objects.create_superuser('admin', 'admin@screwman.test', 'admin')
        User.objects.create_user('usr', 'usr@screwman.test', 'usr')
        Manufacturer.objects.create(title='Test1', description='description')
        Manufacturer.objects.create(title='Test2', description='description2')
    
    def test_authorized_create(self):
        self.client.login(username='user', password='usr')
        response = self.client.post(self.url, {'title': 'test'})
        self.client.logout()

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.login(username='admin', password='admin')
        response = self.client.post(self.url, {'title': 'test'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_authorized_list(self):
        self.client.login(username='usr', password='usr')
        response = self.client.get(self.url)
        self.client.logout()
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        self.client.login(username='admin', password='admin')
        response = self.client.get(self.url)
        self.client.logout()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        

    def test_unauthorized_access(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.post(self.url, {'title': 'test'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        