# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-11 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0012_auto_20170609_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='orden',
            field=models.IntegerField(default=0),
        ),
    ]
