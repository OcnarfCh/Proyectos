# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-14 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rest', '0010_auto_20160814_1537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sucursal',
            name='direccion',
        ),
        migrations.AddField(
            model_name='sucursal',
            name='nombre',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]