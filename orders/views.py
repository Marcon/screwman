from django.utils import timezone
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from .permissions import *


class ManufacturerListView(generics.ListCreateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = [IsAuthenticated, ]


class ManufacturerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = [IsAuthenticated, ]


class DeviceTypeListView(generics.ListCreateAPIView):
    queryset = DeviceType.objects.all()
    serializer_class = DeviceTypeSerializer
    permission_classes = [IsAuthenticated, ]


class DeviceTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeviceType.objects.all()
    serializer_class = DeviceTypeSerializer
    permission_classes = [IsAuthenticated, ]


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
    serializer_class = OrderActionsUpdateSerializer
    permission_classes = [IsAuthenticated, ]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderActionsSerializer
        return super().get_serializer_class()


class OrderActionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderActions.objects.all()
    serializer_class = OrderActionsUpdateSerializer
    permission_classes = [IsAuthenticated, ]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderActionsSerializer
        return super().get_serializer_class()


class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateUpdateSerializer
    permission_classes = [IsAuthenticated, ]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderSerializer
        return super().get_serializer_class()


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateUpdateSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_update(self, serializer):
        if serializer.validated_data['state'] == Order.STATE_DONE and serializer.validated_data['closed_by'] is None:
            serializer.save(closed_by=self.request.user, closed_at=timezone.now())
        else:
            super().perform_update(serializer)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderSerializer
        return super().get_serializer_class()
