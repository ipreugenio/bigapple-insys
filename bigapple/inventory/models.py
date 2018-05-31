from django.db import models
from datetime import date


# Create your models here.

class Supplier(models.Model):
    name = models.CharField('name', max_length=200)
    address = models.CharField('address', max_length=200)
    contact_number = models.CharField('contact_number', max_length=45)


class SupplierItems(models.Model):
    ITEM_TYPES = (
        ('RM', 'Raw Materials'),
        ('MP', 'Machine Parts'),
        ('INK', 'Ink')
    )
    item_name = models.CharField('item_name', max_length=200)
    item_type = models.CharField('item_type', choices=ITEM_TYPES, max_length=200, default='not specified')
    price = models.IntegerField('price')
    description = models.CharField('description', max_length=200)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)


class SupplierPO(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    quantity = models.IntegerField('quantity')
    delivery_date = models.DateField('delivery_date')


class MaterialRequisition(models.Model):
    SHIFTS = (
        ('A', 'shift 1'),
        ('B', 'shift 2'),
        ('C', 'shift 3')
    )
    date_issued = models.DateField('date_issued')
    issued_to = models.CharField('issued_to', max_length=200)
    brand = models.CharField('brand', max_length=200)
    description = models.CharField('description', max_length=200)
    quantity = models.IntegerField('quantity')
    to_be_used_for = models.CharField('to_be_used_for', max_length=200)
    shift = models.CharField('shift', choices=SHIFTS, max_length=200, default='not specified')
    approval = models.BooleanField('approval', default=False)


class PurchaseRequisition(models.Model):
    # placed_by = models.ForeignKey(Accounts.name)
    # department = models.ForeignKey(Accounts.department)
    date_issued = models.DateField('date_issued')
    date_required = models.DateField('date_required')
    # supplier may not be specified on request-- supplier = models.ForeignKey(Supplier, on_delete = models.CASCADE)
    description = models.CharField('description', max_length=200)
    quantity = models.IntegerField('quantity')
    approval = models.BooleanField('approval', default=False)


class Inventory(models.Model):
    RM_TYPES = (
        ('LDPE', 'Low-density polyethylene'),
        ('LLDPE', 'Linear low-density polyethylene'),
        ('HDPE', 'High-density polyethylene'),
        ('PP', 'Polypropylene'),
        ('PET', 'Polyethylene terephthalate')
    )
    rm_name = models.CharField('rm_name', max_length=200, default='not specified')
    rm_type = models.CharField('rm_type', choices=RM_TYPES, max_length=200, default='not specified')
    description = models.CharField('description', max_length=200)
    quantity = models.IntegerField('quantity')


class InventoryCountAsof(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    new_count = models.IntegerField('new_count')
    date_counted = models.DateField('date_counted')
