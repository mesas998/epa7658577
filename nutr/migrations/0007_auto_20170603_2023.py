# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutr', '0006_datasrc_datsrcln'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasrc',
            name='datasrc_id',
            field=models.CharField(db_index=True, max_length=7),
        ),
    ]