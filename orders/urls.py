from django.urls import path
from .views import *

urlpatterns = [
    path('manufacturers/', ManufacturerListView.as_view()),
    path('manufacturers/<int:pk>/', ManufacturerDetailView.as_view()),
    path('device-types/', DeviceTypeListView.as_view()),
    path('device-types/<int:pk>/', DeviceTypeDetailView.as_view()),
    path('actions/', ActionListView.as_view()),
    path('actions/<int:pk>/', ActionDetailView.as_view()),
]