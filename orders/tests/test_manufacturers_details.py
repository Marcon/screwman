from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from orders.models import Manufacturer

User = get_user_model()


class ManufacturersDetailsTest(APITestCase):

    def setUp(self):
        self.url = reverse('manufacturers-details', kwargs={'pk': 1})

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user('usr', 'usr@screwman.test', 'usr')
        Manufacturer.objects.create(title='Test1', description='description')
        Manufacturer.objects.create(title='Test2', description='description2')
    
    def test_unauthorized_access(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.put(self.url, {'title': 'Test3', 'description': 'test'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authorized_retrieve(self):
        self.client.login(username='usr', password='usr')
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authorized_update(self):
        self.client.login(username='usr', password='usr')
        response = self.client.put(self.url, {'title': 'Test3', 'description': 'test'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authorized_delete(self):
        self.client.login(username='usr', password='usr')
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
