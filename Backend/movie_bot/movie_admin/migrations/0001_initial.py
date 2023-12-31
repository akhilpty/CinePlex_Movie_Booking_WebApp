# Generated by Django 4.1.7 on 2023-06-12 11:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie_genres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie_languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie_time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100, null=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('image', models.FileField(upload_to='images')),
                ('is_active', models.SmallIntegerField(default=1)),
                ('trailer', models.CharField(max_length=500)),
                ('genre', models.ManyToManyField(to='movie_admin.movie_genres')),
                ('language', models.ManyToManyField(to='movie_admin.movie_languages')),
                ('time', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie_admin.movie_time')),
            ],
        ),
    ]
