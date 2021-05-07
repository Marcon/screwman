from django.db import models

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


class Order(models.Model):
    device = models.ForeignKey('Device', related_name='orders', on_delete=models.PROTECT)
    accept_date = models.DateTimeField(auto_now_add=True)

