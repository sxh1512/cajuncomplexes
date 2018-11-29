from django import forms
from .models import Apartment, PastPayment, Tenant

class ApartmentAdditionForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = [
            'apt_id',
            'apt_complex',
            'monthly_rent',
            'vacant',
            'tenant_id',
            'maintenance_needed'
        ]

class TenantAdditionForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = [
            'tenant_id',
            'apt_id',
            'tenant_name',
            'next_payment',
            'expected_payment'
        ]