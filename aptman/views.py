from datetime import date
from datetime import datetime as dt
from dateutil.relativedelta import *
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ApartmentAdditionForm, TenantAdditionForm
from .models import Apartment, Tenant

def index(request):
    apartment_list = Apartment.objects.order_by('apt_complex')
    context = {'apartment_list' : apartment_list}
    return render(request, 'aptman/index.html', context)

def details(request, apt_id):
    apt = Apartment.objects.get(pk=apt_id)
    return render(request, 'aptman/details.html', {'apt' : apt})

def add_apartment(request):
    if request.method == 'POST':
        form = ApartmentAdditionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ApartmentAdditionForm()
    
    return render(request, 'aptman/add.html', {'form': form})

def add_tenant(request):
    if request.method == 'POST':
        form = TenantAdditionForm(request.POST)
        if form.is_valid():
            tenant = form.save()
            apt = Apartment.objects.get(pk=tenant.apt_id.apt_id)
            apt.tenant_id = tenant
            apt.vacant = False
            apt.save()
            return HttpResponseRedirect('/')
    else:
        form = TenantAdditionForm()

    return render(request, 'aptman/add.html', {'form': form})

def edit_apt(request, apt_id):
    apt = Apartment.objects.get(pk=apt_id)
    if request.method == 'POST':
        form = ApartmentAdditionForm(request.POST, instance=apt)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ApartmentAdditionForm(instance=apt)
    
    return render(request, 'aptman/add.html', {'form': form})

def edit_tenant(request, tenant_id):
    tenant = Tenant.objects.get(pk=tenant_id)
    if request.method == 'POST':
        form = TenantAdditionForm(request.POST, instance=tenant)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
            form = TenantAdditionForm(instance=tenant)

    return render(request, 'aptman/add.html', {'form': form})

def flag_late(request):
    tenants = Tenant.objects.all()
    late_ids = [tenant.tenant_id for tenant in tenants if (not tenant.last_payment and dt.strptime(str(date.today()), "%Y-%m-%d") > tenant.next_payment_as_dt()) or (tenant.last_payment and tenant.next_payment_as_dt() < tenant.last_payment_as_dt())]
    late_tenants = Tenant.objects.filter(tenant_id__in = late_ids)
    for tenant in late_tenants:
        tenant.missed_payments += 1
        if tenant.missed_payments >= 5:
            tenant.missed_payments = 5
        tenant.expected_payment += tenant.apt_id.monthly_rent
        tenant.next_payment = (dt.strptime(tenant.next_payment, "%m/%d/%Y") + relativedelta(months=1)).strftime("%m/%d/%Y")
        tenant.save()
    context = {'tenants': late_tenants}
    return render(request, 'aptman/late.html', context)
    

def to_evict(request):
    tenants = Tenant.objects.filter(missed_payments = 5)
    context = {'tenants': tenants}
    return render(request, 'aptman/evict.html', context)

def update_history(request):

    pass

def view_history(request):

    pass

def view_tenants(request):
    tenants = Tenant.objects.all()
    context = {'tenants': tenants}
    return render(request, 'aptman/tenants.html', context)

def view_vacant(request):
    vacancies = Apartment.objects.filter(vacant = True).order_by('apt_complex', '-monthly_rent')
    context = {'vacancies': vacancies}
    return render(request, 'aptman/vacant.html', context)

    