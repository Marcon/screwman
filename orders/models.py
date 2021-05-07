from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Manufacturer(models.Model):
    title = models.CharField(max_length=500, unique=True)
    description = models.TextField(null=True)


class DeviceType(models.Model):
    title = models.CharField(max_length=500, unique=True)


class Device(models.Model):
    device_type = models.ForeignKey('DeviceType', on_delete=models.PROTECT)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.PROTECT)
    serial = models.CharField(max_length=200)
    description = models.TextField()


class Action(models.Model):
    title = models.CharField(max_length=500, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True)


class Order(models.Model):
    STATE_NEW = 'new'
    STATE_DIAGNOSTICS = 'diagnostics'
    STATE_CUSTOMER_AGREEMENT = 'agreement'
    STATE_WIP = 'wip'
    STATE_READY = 'ready'
    STATE_DONE = 'done'
    ORDER_STATES = (
        (STATE_NEW, 'New'),
        (STATE_DIAGNOSTICS, 'Diagnostics'),
        (STATE_CUSTOMER_AGREEMENT, 'Customer agreement'),
        (STATE_WIP, 'Work in progress'),
        (STATE_READY, 'Ready'),
        (STATE_DONE, 'Done'),
    )
    device = models.ForeignKey('Device', related_name='orders', on_delete=models.PROTECT)
    accept_date = models.DateTimeField(auto_now_add=True)
    accept_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='+')
    state = models.CharField(max_length=20, choices=ORDER_STATES)
    malfunction_description = models.TextField()
    notes = models.TextField(null=True)
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='+')
    updated_at = models.DateTimeField(auto_now=True)
    closed_by = models.ForeignKey(User, null=True, on_delete=models.PROTECT, related_name='+')
    closed_at = models.DateField(null=True)


class OrderActions(models.Model):
    order = models.ForeignKey('Order', related_name='actions', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    decription = models.TextField()
    action = models.ForeignKey('Action', on_delete=models.PROTECT)
    price = models.DecimalField(null=True, max_digits=10, decimal_places=2)


