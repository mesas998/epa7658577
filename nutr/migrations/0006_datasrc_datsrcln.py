# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 19:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nutr', '0005_auto_20170531_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSrc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datasrc_id', models.IntegerField(db_index=True)),
                ('authors', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=4)),
                ('journal', models.CharField(max_length=135)),
                ('vol_city', models.CharField(max_length=16)),
                ('issue_state', models.CharField(max_length=5)),
                ('start_page', models.CharField(max_length=5)),
                ('end_page', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Datsrcln',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datasrc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutr.DataSrc')),
                ('ndb_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutr.NutrDef')),
                ('nutr_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutr.NutData')),
            ],
        ),
    ]
