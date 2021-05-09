from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from orders.models import Order, Customer, Device, DeviceType, Manufacturer

User = get_user_model()


class OrdersList(APITestCase):

    def setUp(self):
        self.url = reverse('orders-details', kwargs={'pk': 1})

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user('usr', 'usr@screwman.test', 'usr')
        manufacturer = Manufacturer.objects.create(title='Test', description='Test manufacturer')
        device_type = DeviceType.objects.create(title='cell phone')
        device1 = Device.objects.create(device_type=device_type, manufacturer=manufacturer, serial='sn-00001', model='d-00001', description='test device')
        device2 = Device.objects.create(device_type=device_type, manufacturer=manufacturer, serial='sn-00002', model='d-00002', description='test device')
        customer1 = Customer.objects.create(name='Customer 1', phone='+380000000')
        customer2 = Customer.objects.create(name='Customer 2', phone='+380000001')
        Order.objects.create(customer=customer1, device=device1, accept_by=user, state=Order.STATE_NEW, malfunction_description='description', updated_by=user)
        Order.objects.create(customer=customer2, device=device2, accept_by=user, state=Order.STATE_NEW, malfunction_description='description', updated_by=user)

    def test_unauthenticated_access(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.put(self.url, {'customer': 1, 'device': 1, 'state': Order.STATE_NEW, 'malfunction_description': 'description'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_get(self):
        self.client.login(username='usr', password='usr')
        response = self.client.get(self.url)
        self.client.logout()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_put(self):
        self.client.login(username='usr', password='usr')
        response = self.client.put(self.url, {'customer': 1, 'device': 1, 'state': Order.STATE_DIAGNOSTICS, 'malfunction_description': 'description'})
        self.client.logout()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_delete(self):
        self.client.login(username='usr', password='usr')
        response = self.client.delete(self.url)
        self.client.logout()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
