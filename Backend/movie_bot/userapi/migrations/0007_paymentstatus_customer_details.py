# Generated by Django 4.1.7 on 2023-06-15 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapi', '0006_remove_paymentstatus_customer_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentstatus',
            name='customer_details',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userapi.booking'),
        ),
    ]
