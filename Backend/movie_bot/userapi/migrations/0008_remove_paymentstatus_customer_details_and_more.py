# Generated by Django 4.1.7 on 2023-06-15 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapi', '0007_paymentstatus_customer_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentstatus',
            name='customer_details',
        ),
        migrations.AddField(
            model_name='paymentstatus',
            name='movie_id',
            field=models.IntegerField(null=True),
        ),
    ]
