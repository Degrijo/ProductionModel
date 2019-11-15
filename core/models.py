from django.db import models


class Inventory(models.Model):
    WORK_CLOTHES = 'WC'
    TOOL = 'TL'
    AUXILIARY_MEANS = 'AM'
    OTHER = 'OT'
    TYPE_CHOICES = [(WORK_CLOTHES, 'work clothes'), (TOOL, 'tools'), (AUXILIARY_MEANS, 'auxiliary means'), (OTHER, 'other')]
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default=OTHER)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name + ' ' + dict(self.TYPE_CHOICES)[self.type]


class Stock(models.Model):
    name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=15)
    inventories = models.ManyToManyField(Inventory, 'stocks')

    def __str__(self):
        return self.name


class Waybill(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    inventories = models.ManyToManyField(Inventory, 'waybills', through='InventoryWaybill')
    employee_name = models.CharField(max_length=200)
    employee_position = models.CharField(max_length=50)
    incoming = models.BooleanField(blank=False, null=False)


class InventoryWaybill(models.Model):
    inventory = models.ForeignKey(Inventory, models.CASCADE, 'inventory_waybill')
    waybill = models.ForeignKey(Waybill, models.CASCADE, 'inventory_waybill')
    inventory_number = models.PositiveIntegerField()
