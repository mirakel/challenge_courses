# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-17 17:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0002_auto_20171217_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito_compra',
            name='precio_total',
        ),
    ]