from django.contrib import admin

from .models import Supplier, Product, ClientPO, ClientItem, ClientCreditStatus
# Register your models here.

admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(ClientPO)
admin.site.register(ClientItem)
admin.site.register(ClientCreditStatus)