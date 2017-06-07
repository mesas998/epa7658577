from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.text import slugify

SLUG_LENGTH = 3


def add_slug_data(apps, schema_editor):
    NutrDef = apps.get_model(
        'nutr', 'NutrDef')
    query = NutrDef.objects.all()
    for nutrdef in query:
        expected_slug = slugify(nutrdef.nutr_no)
        rivals = (
            NutrDef.objects.filter(
                slug__startswith=expected_slug
            ).count())
        if rivals > 0:
            str_len = (
                SLUG_LENGTH - len(str(rivals)))
            nutrdef.slug = "{}-{}".format(
                expected_slug[:str_len - 1],
                rivals + 1)
        else:
            nutrdef.slug = expected_slug
        nutrdef.save()


def remove_slug_data(apps, schema_editor):
    NutrDef = apps.get_model(
        'nutr', 'NutrDef')
    NutrDef.objects.update(slug='')


class Migration(migrations.Migration):

    dependencies = [
        ('nutr', '0003_auto_20170524_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='nutrdef',
            name='slug',
            field=models.SlugField(
                max_length=SLUG_LENGTH,
                default=''),
        ),
        migrations.RunPython(
            add_slug_data,
            reverse_code=remove_slug_data
        ),
        migrations.AlterField(
            model_name='nutrdef',
            name='slug',
            field=models.SlugField(
                max_length=SLUG_LENGTH),
        ),
    ]

