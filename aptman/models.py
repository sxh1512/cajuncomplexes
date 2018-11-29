from django.db import models

# Create your models here.

class Apartment(models.Model):
    apt_id = models.IntegerField(primary_key=True)
    apt_complex = models.CharField(max_length=200)
    monthly_rent = models.DecimalField(decimal_places=2, max_digits=25)
    vacant = models.BooleanField(default=True)
    tenant_id = models.ForeignKey('Tenant', on_delete=models.CASCADE, null=True)
    maintenance_needed = models.BooleanField(default=False)

    def get_tenant(self):
        if self.tenant_id:
            return "\nTenant ID: " + str(self.tenant_id)
        else:
            return ""

    def yes_no(self, val):
        ret = "Yes" if val else "No"
        return ret

    def __str__(self):
        val = "Complex: " + self.apt_complex + "\nApartment ID: " + str(self.apt_id) + "\nRent: $" + str(self.monthly_rent) + "\nVacant: " + self.yes_no(self.vacant) + self.get_tenant() + "\nNeeds Maintenance: " + self.yes_no(self.maintenance_needed)
        return val 


class Tenant(models.Model):
    tenant_id = models.IntegerField(primary_key=True)
    apt_id = models.ForeignKey(Apartment, on_delete=models.CASCADE, null=True, blank=True)
    tenant_name = models.CharField(max_length=200)
    last_payment = models.CharField(max_length=10)
    next_payment = models.CharField(max_length=10)
    expected_payment = models.DecimalField(decimal_places=2, max_digits=25)
    missed_payments = models.IntegerField(default=0)

    def __str__(self):
        return str(self.tenant_id) + ": " + self.tenant_name


class PastPayment(models.Model):
    tenant_id = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    payment_date = models.DateField()
    payment_amount = models.DecimalField(decimal_places=2, max_digits=25)


"""
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date publishsed')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
"""