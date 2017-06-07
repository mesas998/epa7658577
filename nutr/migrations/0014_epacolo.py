# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 22:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutr', '0013_auto_20170603_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='EPAColo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ffdru', models.CharField(max_length=63)),
                ('fregid', models.CharField(max_length=12)),
                ('fsn', models.CharField(max_length=80)),
                ('slt', models.CharField(max_length=50)),
                ('loc', models.CharField(max_length=60)),
                ('county', models.CharField(max_length=35)),
                ('fips', models.CharField(max_length=5)),
                ('usps', models.CharField(max_length=2)),
                ('state', models.CharField(max_length=35)),
                ('country', models.CharField(max_length=44)),
                ('postal', models.CharField(max_length=14)),
                ('ffic', models.CharField(max_length=50)),
                ('fan', models.CharField(max_length=50)),
                ('tribe', models.CharField(max_length=3)),
                ('tln', models.CharField(max_length=80)),
                ('cdn', models.CharField(max_length=2)),
                ('huc', models.CharField(max_length=8)),
                ('region', models.CharField(max_length=2)),
                ('type', models.CharField(max_length=40)),
                ('desc', models.CharField(max_length=80)),
                ('cdate', models.DateField()),
                ('udate', models.DateField()),
                ('mex', models.CharField(max_length=3)),
                ('abbrev', models.CharField(max_length=80)),
                ('eit', models.CharField(max_length=80)),
                ('naics', models.CharField(max_length=80)),
                ('ntext', models.CharField(max_length=80)),
                ('sic', models.CharField(max_length=80)),
                ('sict', models.CharField(max_length=80)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('long', models.DecimalField(decimal_places=6, max_digits=10)),
                ('conv', models.CharField(max_length=25)),
                ('hcmt', models.CharField(max_length=60)),
                ('ham', models.IntegerField()),
                ('rpn', models.CharField(max_length=40)),
                ('hrdn', models.CharField(max_length=5)),
                ('cdsn', models.CharField(max_length=35)),
                ('cbc', models.CharField(max_length=15)),
            ],
        ),
    ]