# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-21 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rest', '0025_auto_20160820_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sucursal',
            name='image',
            field=models.FileField(default=1, upload_to='albums/images/'),
            preserve_default=False,
        ),
    ]
