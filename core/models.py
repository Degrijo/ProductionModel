from django.db import models


class Inventory(models.Model):
    WORK_CLOTHES = 'WC'
    TOOL = 'TL'
    AUXILIARY_MEANS = 'AM'
    OTHER = 'OT'
    TYPE_CHOICES = [(WORK_CLOTHES, 'work clothes'), (TOOL, 'tools'), (AUXILIARY_MEANS, 'auxiliary means'), (OTHER, 'other')]
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default=OTHER)
    name = models.CharField(max_length=200, default="")

    def __str__(self):
        return f'{self.name} [{dict(self.TYPE_CHOICES)[self.type]}]'


class Stock(models.Model):
    name = models.CharField(max_length=120, default="")
    phone_number = models.CharField(max_length=15)
    inventories = models.ManyToManyField(Inventory, 'stocks', through='InventoryWaybillStock')

    def __str__(self):
        return self.name


class Waybill(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    employee_name = models.CharField(max_length=200)
    employee_position = models.CharField(max_length=50)
    incoming = models.BooleanField(blank=False, null=False)
    inventories = models.ManyToManyField(Inventory, 'waybills', through='InventoryWaybillStock')

    def __str__(self):
        return f'Waybill №{self.id}'


class InventoryWaybillStock(models.Model):
    inventory = models.ForeignKey(Inventory, models.CASCADE, 'inventory_waybill_stock')
    waybill = models.ForeignKey(Waybill, models.CASCADE, 'inventory_waybill_stock')
    stock = models.ForeignKey(Stock, models.CASCADE, 'inventory_waybill_stock')
    inventory_number = models.IntegerField()
