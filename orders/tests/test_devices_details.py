from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from orders.models import Device, DeviceType, Manufacturer

User = get_user_model()


class DevicesList(APITestCase):

    def setUp(self):
        self.url = reverse('devices-details', kwargs={'pk': 1})

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user('usr', 'usr@screwman.test', 'usr')
        manufacturer = Manufacturer.objects.create(title='Test', description='Test manufacturer')
        device_type = DeviceType.objects.create(title='cell phone')
        Device.objects.create(device_type=device_type, manufacturer=manufacturer, serial='sn-00001', model='d-00001', description='test device')
        Device.objects.create(device_type=device_type, manufacturer=manufacturer, serial='sn-00002', model='d-00002', description='test device')

    def test_unauthenticated_access(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.put(self.url, {'device_type': 1, 'manufacturer': 1, 'serial': 'sn-00003', 'model': 'd-00003', 'description': 'test device'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_get(self):
        self.client.login(username='usr', password='usr')
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_update(self):
        self.client.login(username='usr', password='usr')
        response = self.client.put(self.url, {'device_type': 1, 'manufacturer': 1, 'serial': 'sn-00003', 'model': 'd-00003', 'description': 'test device'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_delete(self):
        self.client.login(username='usr', password='usr')
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
