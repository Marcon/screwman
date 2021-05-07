from django.urls import path, include

urlpatterns = [
    path('v1/orders/', include('orders.urls')),
]
