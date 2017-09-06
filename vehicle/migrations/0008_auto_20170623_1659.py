# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-23 16:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0007_auto_20170623_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinbox',
            name='from_time',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='userinbox',
            name='to_time',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='userinbox',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='vehicle.UserProfile'),
        ),
    ]