# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-01 16:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0015_auto_20170701_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinbox',
            name='veh',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicle.Vehicle'),
        ),
    ]
