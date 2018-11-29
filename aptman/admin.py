from django.contrib import admin

from .models import Apartment, Tenant, PastPayment

admin.site.register(Apartment)
admin.site.register(Tenant)
admin.site.register(PastPayment)
