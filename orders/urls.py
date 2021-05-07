from django.urls import path
from .views import *

urlpatterns = [
    path('manufacturers/', ManufacturerListView.as_view()),
    path('manufacturers/<int:pk>/', ManufacturerDetailView.as_view()),
    path('device-types/', DeviceTypeListView.as_view()),
    path('device-types/<int:pk>/', DeviceTypeDetailView.as_view()),
    path('actions/', ActionListView.as_view()),
    path('actions/<int:pk>/', ActionDetailView.as_view()),
    path('customers/', CustomerListView.as_view()),
    path('customers/<int:pk>/', CustomerDetailView.as_view()),
    path('devices/', DeviceListView.as_view()),
    path('devices/<int:pk>/', DeviceListView.as_view()),
    path('order-actions/', OrderActionListView.as_view()),
    path('order-actions/<int:pk>/', OrderActionDetailView.as_view()),
    path('', OrderListView.as_view()),
    path('<int:pk>/', OrderDetailView.as_view()),
]