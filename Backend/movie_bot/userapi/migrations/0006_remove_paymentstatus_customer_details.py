# Generated by Django 4.1.7 on 2023-06-15 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapi', '0005_remove_paymentstatus_payment_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentstatus',
            name='customer_details',
        ),
    ]