
from django.forms import ModelForm, ValidationError
from .models import ClientItem, ClientPO, Product, Client
from decimal import Decimal
from django.contrib.admin.widgets import AdminDateWidget

from django import forms
from .models import ClientItem, ClientPO, Product, Supplier



class ClientPOFormItems(ModelForm):

    class Meta:
        model = ClientItem
        fields = ('products', 'laminate', 'width', 'length', 'color', 'gusset', 'quantity')


class ClientPOForm(ModelForm):

    class Meta:
        model = ClientPO
        fields = ('terms', 'other_info')
        #widgets = {'date_required':DateTimePicker(options={"format": "YYYY-MM-DD", "pickSeconds": False}}

        fields = '__all__'
		

class AddSupplier_Form(forms.Form):    
    model = Supplier
    fields = ('company_name', 'contact_person', 'department', 'mobile_number', 'email_address',
    'supplier_type', 'description')

        

