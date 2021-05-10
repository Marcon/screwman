from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from orders.models import Customer

User = get_user_model()


class CustomersList(APITestCase):

    def setUp(self):
        self.url = reverse('customers-list')

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user('usr', 'usr@screwman.test', 'usr')
        Customer.objects.create(name='Test customer', phone='+380000000', email='test@screwman.test')

    def test_unauthorized_access(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_get(self):
        self.client.login(username='usr', password='usr')
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_create(self):
        self.client.login(username='usr', password='usr')
        response = self.client.post(self.url, {'name': 'Test customer', 'phone': '+380000001'})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_should_restrict_duplicate_phone(self):
        self.client.login(username='usr', password='usr')
        response = self.client.post(self.url, {'name': 'Duplicate Phone', 'phone': '+380000000'})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_should_restrict_duplicate_email(self):
        self.client.login(username='usr', password='usr')
        response = self.client.post(self.url, {'name': 'Duplicate email', 'phone': '+380000002', 'email': 'test@screwman.test'})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)