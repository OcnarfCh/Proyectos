# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-24 04:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rest', '0028_auto_20160824_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sucursal',
            name='latitud',
            field=models.DecimalField(decimal_places=5, max_digits=5),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='longitud',
            field=models.DecimalField(decimal_places=5, max_digits=5),
        ),
    ]
