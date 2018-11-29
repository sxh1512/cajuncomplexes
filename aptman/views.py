from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ApartmentAdditionForm
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
