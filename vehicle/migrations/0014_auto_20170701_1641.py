# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-01 16:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0013_vehicle_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinbox',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.Vehicle'),
        ),
    ]
