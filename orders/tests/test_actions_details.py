from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from orders.models import Action

User = get_user_model()


class ActionsList(APITestCase):

    def setUp(self):
        self.url = reverse('actions-details', kwargs={'pk': 1})

    @classmethod
    def setUpTestData(cls):
        User.objects.create_superuser('admin', 'admin@screwman.test', 'admin')
        User.objects.create_user('usr', 'usr@screwman.test', 'usr')
        Action.objects.create(title='test_action', price=100.0)

    def test_unauthorized_access(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.put(self.url, {'title': 'test_action', 'price': 50.0})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_get(self):
        self.client.login(username='usr', password='usr')
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_non_admin_update(self):
        self.client.login(username='usr', password='usr')

        response = self.client.put(self.url, {'title': 'test', 'price': 200.0})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_update(self):
        self.client.login(username='admin', password='admin')
        response = self.client.put(self.url, {'title': 'test', 'price': 200.0})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_admin_delete(self):
        self.client.login(username='admin', password='admin')
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
