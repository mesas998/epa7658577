# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutr', '0008_auto_20170603_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datsrcln',
            name='nutr_no',
            field=models.IntegerField(db_index=True),
        ),
    ]
