# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutr', '0004_nutrdef_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nutrdef',
            options={'ordering': ['-nutr_no'], 'verbose_name': 'nutrient'},
        ),
        migrations.AlterField(
            model_name='nutrdef',
            name='slug',
            field=models.SlugField(help_text='A label for URL config.', max_length=3, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='nutrdef',
            unique_together=set([('slug',)]),
        ),
    ]