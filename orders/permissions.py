from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import Order


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff


class ClosedOrderAdminWriteable(BasePermission):
    def has_permission(self, request, view):
        obj = view.get_object()
        if request.method in SAFE_METHODS:
            return True
        if obj.state == Order.STATE_DONE:
            return request.user.is_staff
        return True
