from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ApartmentAdditionForm, TenantAdditionForm
from .models import Apartment

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

def view_vacant(request):
    vacancies = Apartment.objects.filter(vacant = True).order_by('apt_complex', '-monthly_rent')
    context = {'vacancies': vacancies}
    return render(request, 'aptman/vacant.html', context)

    