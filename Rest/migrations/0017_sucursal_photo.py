# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-20 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rest', '0016_auto_20160814_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='sucursal',
            name='photo',
            field=models.ImageField(default=1, upload_to='cars'),
            preserve_default=False,
        ),
    ]
