from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from .permissions import *

class ManufacturerListView(generics.ListCreateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly, ]


class ManufacturerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly, ]


class DeviceTypeListView(generics.ListCreateAPIView):
    queryset = DeviceType.objects.all()
    serializer_class = DeviceTypeSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly, ]

class DeviceTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeviceType.objects.all()
    serializer_class = DeviceTypeSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly, ]


class ActionListView(generics.ListCreateAPIView):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly, ]


class ActionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly, ]


class CustomerListView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated, ]


class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated, ]


class DeviceListView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated, ]


class DeviceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated, ]


class OrderActionListView(generics.ListCreateAPIView):
    queryset = OrderActions.objects.all()
    serializer_class = OrderActionsSerializer
    permission_classes = [IsAuthenticated, ]


class OrderActionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderActions.objects.all()
    serializer_class = OrderActionsSerializer
    permission_classes = [IsAuthenticated, ]


class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, ]


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, ]
