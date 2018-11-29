from django.http import HttpResponse
from django.shortcuts import render
from .models import Apartment

def index(request):
    apartment_list = Apartment.objects.order_by('apt_id')
    context = {'apartment_list' : apartment_list}
    return render(request, 'aptman/index.html', context)

def details(request, apt_id):
    apt = Apartment.objects.get(pk=apt_id)
    return render(request, 'aptman/details.html', {'apt' : apt})