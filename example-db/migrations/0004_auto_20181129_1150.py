# Generated by Django 2.1.2 on 2018-11-29 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aptman', '0003_auto_20181129_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pastpayment',
            name='payment_date',
            field=models.CharField(max_length=10),
        ),
    ]
