# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-23 18:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0008_auto_20170623_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinbox',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
