from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from orders.models import Customer

User = get_user_model()


class CustomersList(APITestCase):

    def setUp(self):
        self.url = reverse('customers-details', kwargs={'pk': 1})

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user('usr', 'usr@screwman.test', 'usr')
        Customer.objects.create(name='Test customer', phone='+380000000', email='test@screwman.test')
        Customer.objects.create(name='Test customer', phone='+380000001', email='test1@screwman.test')
        Customer.objects.create(name='Test customer', phone='+380000002', email='test2@screwman.test')

    def test_unauthorized_access(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.put(self.url, {'name': 'Test customer', 'phone': '+380000003', 'email': 'test@screwman.test'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_get(self):
        self.client.login(username='usr', password='usr')
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_update(self):
        self.client.login(username='usr', password='usr')
        response = self.client.put(self.url, {'name': 'Test Customer', 'phone': '+380000010', 'email': 'test@screwman.test'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_delete(self):
        self.client.login(username='usr', password='usr')
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_should_restrict_duplicate_email(self):
        url = reverse('customers-details', kwargs={'pk': 2})
        self.client.login(username='usr', password='usr')
        response = self.client.put(url, {'name': 'Test Customer', 'phone': '+380000001', 'email': 'test2@screwman.test'})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)