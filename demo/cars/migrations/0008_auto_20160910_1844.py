# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-10 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_auto_20160910_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='foldable_rear_seat',
            field=models.NullBooleanField(),
        ),
    ]