from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from orders.models import DeviceType

User = get_user_model()


class DeviceTypesList(APITestCase):

    def setUp(self):
        self.url = reverse('device-types-list')

    @classmethod
    def setUpTestData(cls):
        User.objects.create_superuser('admin', 'admin@screwman.test', 'admin')
        User.objects.create_user('usr', 'usr@screwman.test', 'usr')
        DeviceType.objects.create(title='test1')
        DeviceType.objects.create(title='test2')

    def test_unauthorized_access(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.post(self.url, {'title': 'test3'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_get(self):
        self.client.login(username='usr', password='usr')
        response = self.client.get(self.url)
        self.client.logout()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_non_admin_create(self):
        self.client.login(username='usr', password='url')
        response = self.client.post(self.url, {'title': 'test3'})
        self.client.logout()

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_admin_create(self):
        self.client.login(username='admin', password='admin')
        response = self.client.post(self.url, {'title': 'test3'})
        self.client.logout()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
