# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutr', '0009_auto_20170603_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datsrcln',
            name='datasrc_id',
            field=models.CharField(max_length=6),
        ),
    ]
