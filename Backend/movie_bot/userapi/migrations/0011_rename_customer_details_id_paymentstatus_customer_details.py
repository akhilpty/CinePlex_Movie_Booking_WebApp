# Generated by Django 4.1.7 on 2023-06-15 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapi', '0010_rename_customer_details_paymentstatus_customer_details_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymentstatus',
            old_name='customer_details_id',
            new_name='customer_details',
        ),
    ]
