# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-06 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0023_feedbackreply_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedbackreply',
            name='status',
        ),
        migrations.AddField(
            model_name='feedback',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
