from django.db import models

# Create your models here.

class Apartment(models.Model):
    apt_id = models.IntegerField(primary_key=True)
    apt_complex = models.CharField(max_length=200)
    monthly_rent = models.DecimalField(decimal_places=2, max_digits=25)
    vacant = models.BooleanField(default=True)
    tenant_id = models.ForeignKey('Tenant', on_delete=models.CASCADE, null=True, blank=True)
    maintenance_needed = models.BooleanField(default=False)

    def __str__(self):
        return self.apt_complex + ": " + str(self.apt_id)

class Tenant(models.Model):
    tenant_id = models.IntegerField(primary_key=True)
    apt_id = models.ForeignKey(Apartment, on_delete=models.CASCADE, null=True, blank=True)
    tenant_name = models.CharField(max_length=200)
    last_payment = models.DateField()
    next_payment = models.DateField()
    expected_payment = models.DecimalField(decimal_places=2, max_digits=25)
    missed_payments = models.IntegerField()

    def __str__(self):
        return self.tenant_name


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