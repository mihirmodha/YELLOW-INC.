# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-13 09:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cars', '0012_userprofile_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField()),
                ('manufacturer', models.CharField(blank=True, choices=[('Audi', 'Audi'), ('Maruti-Suzuki', 'Maruti-Suzuki'), ('Tata Motors', 'Tata Motors'), ('Hyundai', 'Hyundai'), ('Honda', 'Honda'), ('Volkswagen', 'Volkswagen'), ('Toyota', 'Toyota'), ('Mahindra', 'Mahindra'), ('Renault', 'Renault'), ('Fiat', 'Fiat'), ('Chevrolet', 'Chevrolet'), ('Ford', 'Ford'), ('KIA', 'KIA'), ('Porsche', 'Porsche'), ('Nissan', 'Nissan')], max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
