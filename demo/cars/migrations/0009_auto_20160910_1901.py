# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-10 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_auto_20160910_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='foldable_rear_seat',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]