from django.urls import path
from .views import *

urlpatterns = [
    path('manufacturers/', ManufacturerListView.as_view())
]