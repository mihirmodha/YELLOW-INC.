# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-13 07:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0011_auto_20160913_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='DOB',
            field=models.DateField(default=datetime.datetime(2016, 9, 13, 13, 22, 23, 710459)),
            preserve_default=False,
        ),
    ]
