from django.db import models
from django.forms import ModelForm, BaseModelFormSet
from datetime import date
from django.urls import reverse
from accounts.models import Client
from decimal import Decimal
from datetime import date

# Create your models here.

class Product(models.Model):
    products = models.CharField('products', max_length=200)
    prod_price = models.DecimalField('prod_price', decimal_places=3, max_digits=12, default=0)
    description = models.CharField('description', max_length=200)

    def __str__(self):
        return self.products + " : Php." + str(self.prod_price) + "/piece"



#could be substitute for quotation request
class ClientPO(models.Model):
    date_issued = models.DateTimeField('date_issued', auto_now_add=True, blank=True)
    date_required = models.DateTimeField('date_required', auto_now_add=True, blank=True)
    note = models.CharField('note', max_length=200, default='')
    terms = models.CharField('terms', max_length=250)
    other_info = models.CharField('other_info', max_length=250)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    total_amount = models.DecimalField('total_amount', default=0, decimal_places=3, max_digits=12)
    confirmed = models.BooleanField('confirmed', default=False)
    d0 = date(date_issued)
    d1 = date(date_required)
    lead_time = d1 - d0

    def __str__(self):
        return 'PO_%s' % (self.id)


class ClientItem(models.Model):

    COLOR =(
        ('R', 'Red'),
        ('B', 'Blue'),
        ('Y', 'Yellow'),
        ('O', 'Orange'),
        ('G', 'Green'),
        ('V', 'Violet'),
        ('Blk', 'Black'),
        ('Wht', 'White'),
        ('P', 'Plain')
    )

    products = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    laminate = models.BooleanField('laminate', default=False)
    width = models.DecimalField('width', decimal_places=3, max_digits=12)
    length = models.DecimalField('length', decimal_places=3, max_digits=12)
    color = models.CharField('color', choices=COLOR, max_length=200)
    gusset = models.DecimalField('gusset', decimal_places=3, max_digits=12)
    quantity = models.IntegerField('quantity')
    item_price = models.DecimalField('price', decimal_places=3, max_digits=12, default=0)
    client_po = models.ForeignKey(ClientPO, on_delete=models.CASCADE, null=True)
    # sample_layout = models.CharField('sample_layout', max_length=200)

    def get_absolute_url(self):
        return reverse('accounts:user-page-view')

    def __str__(self):
        return self.id


    def calculate_item_total(self):
        total = Decimal('0.0')
        total += (self.products.prod_price * self.quantity)
        return total

    def save(self, *args, **kwargs):
        if self.products is not None:
            self.item_price = self.calculate_item_total()
        else:
            self.item_price = Decimal(0.0)
        super(ClientItem, self).save(*args, **kwargs)


# class CostingSheet(models.Model)



class SalesInvoice(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    client_po = models.ForeignKey(ClientPO, on_delete=models.CASCADE)
    date_issued = models.DateField('date_issued', auto_now_add=True, blank=True)
    total_amount = models.DecimalField('total_amount', blank=True, decimal_places=3, max_digits=12)
    discount = models.DecimalField('discount', blank=True, decimal_places=3, max_digits=12)
    net_vat = models.DecimalField('net_vat', blank=True, decimal_places=3, max_digits=12)
    amount_due = models.DecimalField('amount_due', blank=True, decimal_places=3, max_digits=12)

class ClientCreditStatus(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    credit_status = models.BooleanField('credit_status', default=True)
    outstanding_balance = models.DecimalField('outstanding_balance', decimal_places=3, max_digits=12)
    invoice_issued = models.ForeignKey(SalesInvoice, on_delete=models.CASCADE)
    total_paid = models.DecimalField('total_paid', decimal_places=3, max_digits=12)
    date_due = models.DateField('date_due', auto_now_add=True, blank=True)

    class Meta:
        verbose_name_plural = "Client credit status"

class Supplier(models.Model):
    DEPARTMENT = (
        ('AF', 'Accounting and Finance'),
        ('HR', 'Human Resource'),
        ('IT', 'Information Technology'),
        ('M', 'Marketing'),
        ('P', 'Purchasing'),
        ('RD', 'Research and Development'),
        ('S', 'Sales'),
        ('O', 'Others'),

    )

    SUPPLIERTYPE = (
        ('RM', 'Raw Material'),
        ('MP', 'Machinery/Parts'),
        ('I', 'Ink'),
        ('O', 'Others'),

    )

    company_name = models.CharField('company_name', max_length=200)
    contact_person = models.CharField('contact_person', max_length=200)
    mobile_number = models.CharField('mobile_number', max_length=11)
    email_address = models.CharField('email_address', max_length=200)
    description = models.CharField('description', max_length=200, blank =True)
    supplier_type = models.CharField('suppier_type', choices=SUPPLIERTYPE, max_length=200, default='not specified')
    department = models.CharField('department', choices=DEPARTMENT, max_length=200, default='not specified')

    def __str__(self):
        return self.company_name
