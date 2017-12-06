# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-05 17:17
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models
import oscar.models.fields.autoslugfield


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0004_auto_20170226_1122'),
        ('shipping', '0003_fletedefault'),
    ]

    operations = [
        migrations.CreateModel(
            name='StandardMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', oscar.models.fields.autoslugfield.AutoSlugField(blank=True, editable=False, max_length=128, populate_from=b'name', unique=True, verbose_name='Slug')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('price_per_order', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=12, verbose_name='Price per order')),
                ('price_per_item', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=12, verbose_name='Price per item')),
                ('free_shipping_threshold', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Free Shipping')),
                ('countries', models.ManyToManyField(blank=True, to='address.Country', verbose_name='Countries')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
                'verbose_name': 'Shipping method',
                'verbose_name_plural': 'Shipping methods',
            },
        ),
        migrations.RemoveField(
            model_name='fletedefault',
            name='countries',
        ),
        migrations.DeleteModel(
            name='FleteDefault',
        ),
    ]