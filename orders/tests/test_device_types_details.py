from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from orders.models import DeviceType

User = get_user_model()


class DeviceTypesList(APITestCase):

    def setUp(self):
        self.url = reverse('device-types-details', kwargs={'pk': 1})

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user('usr', 'usr@screwman.test', 'usr')
        DeviceType.objects.create(title='test1')
        DeviceType.objects.create(title='test2')

    def test_unauthorized_access(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.put(self.url, {'title': 'test3'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authorized_get(self):
        self.client.login(username='usr', password='usr')
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_put(self):
        self.client.login(username='usr', password='usr')
        response = self.client.put(self.url, {'title': 'test3'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_delete(self):
        self.client.login(username='usr', password='usr')
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
