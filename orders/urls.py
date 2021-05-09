from django.urls import path
from .views import *

urlpatterns = [
    path('manufacturers/', ManufacturerListView.as_view(), name='manufacturers-list'),
    path('manufacturers/<int:pk>/', ManufacturerDetailView.as_view(), name='manufacturers-details'),
    path('device-types/', DeviceTypeListView.as_view(), name='device-types-list'),
    path('device-types/<int:pk>/', DeviceTypeDetailView.as_view(), name='device-types-details'),
    path('actions/', ActionListView.as_view(), name='actions-list'),
    path('actions/<int:pk>/', ActionDetailView.as_view(), name='actions-details'),
    path('customers/', CustomerListView.as_view(), name='customers-list'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customers-details'),
    path('devices/', DeviceListView.as_view(), name='devices-list'),
    path('devices/<int:pk>/', DeviceDetailView.as_view(), name='devices-details'),
    path('order-actions/', OrderActionListView.as_view(), name='order-actions-list'),
    path('order-actions/<int:pk>/', OrderActionDetailView.as_view(), name='order-actions-details'),
    path('', OrderListView.as_view(), name='orders-list'),
    path('<int:pk>/', OrderDetailView.as_view(), name='orders-details'),
]