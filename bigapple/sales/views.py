from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, reverse, HttpResponseRedirect
from bigapple.apps.production.models import JobOrder

from .models import Supplier, ClientItem, ClientPO, ClientCreditStatus, Client
from .forms import AddSupplier_Form

# Create your views here.
def sales_details(request):
    context = {
        'title': 'Sales Content'
    }

    return render(request, 'sales/sales_details.html', context)

def supplier_list(request):
    query = Supplier.objects.all() 
    
    context = {
        'query' : query,
    }
    return render(request, 'sales/supplier_list.html', context)

def add_supplier(request):
    query = Supplier.objects.all() 
    context = {
        'title' : "New Supplier",
        'actiontype' : "Add",
        'query' : query,
    }

    if request.method == 'POST':
        company_name = request.POST['company_name']
        contact_person = request.POST['contact_person']
        department = request.POST['department']
        mobile_number = request.POST['mobile_number']
        email_address = request.POST['email_address']
        supplier_type = request.POST['supplier_type']
        description = request.POST['description']

        result = Supplier(company_name=company_name, contact_person=contact_person, department=department,
        mobile_number=mobile_number, email_address=email_address, supplier_type=supplier_type, description=description)
        result.save()
        return HttpResponseRedirect('../supplier_list')
    
    else:
        return render(request, 'sales/add_supplier.html', context)

def edit_supplier(request, id):
    supplier = Supplier.objects.get(id=id)
    
    context = {
        'title' : "Edit Supplier",
        'actiontype' : "Edit",
        'supplier' : supplier,
    }

    return render(request, 'sales/edit_supplier.html/', context)

def delete_supplier(request, id):
    supplier = Supplier.objects.get(id=id)
    supplier.delete()
    return HttpResponseRedirect('../supplier_list')

class POListView(generic.ListView):
    model = ClientPO
    all_PO = ClientPO.objects.all()
    template_name = 'sales/clientPO_list.html'

class PODetailView(generic.DetailView):
    model = ClientPO
    template_name = 'sales/clientPO_details.html'


class POFormCreateView(CreateView):
    model = ClientItem
    template_name = 'sales/clientPO_form.html'
    fields = ('products', 'note', 'width', 'length', 'color', 'gusset', 'quantity')

class JOListView(generic.ListView):
    model = JobOrder
    all_JO = JobOrder.objects.all()
    template_name = 'sales/JO_list.html'

