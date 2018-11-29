from django.db import models

# Create your models here.

class Apartments(models.Model):
    apt_id = models.IntegerField(primary_key=True)
    apt_complex = models.CharField(max_length=200)
    monthly_rent = models.DecimalField(decimal_places=2, max_digits=25)
    vacant = models.BooleanField(default=True)
    tenant = models.CharField(max_length=200, default=None)
    maintenance_needed = models.BooleanField(default=False)

    def __str__(self):
        return self.apt_complex + ": " + str(self.apt_id)

class Tenants(models.Model):
    tenant_id = models.IntegerField(primary_key=True)
    apt_id = models.ForeignKey(Apartments, on_delete=models.CASCADE)
    tenant_name = models.CharField(max_length=200)
    last_payment = models.DateField()
    next_payment = models.DateField()
    expected_payment = models.DecimalField(decimal_places=2, max_digits=25)
    missed_payments = models.IntegerField()

    def __str__(self):
        return self.tenant_name


class PaymentHistory(models.Model):
    tenant_id = models.ForeignKey(Tenants, on_delete=models.CASCADE)
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