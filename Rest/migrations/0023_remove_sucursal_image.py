# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-20 17:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Rest', '0022_sucursal_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sucursal',
            name='image',
        ),
    ]
