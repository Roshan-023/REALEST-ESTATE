# Generated by Django 4.2.7 on 2023-12-16 08:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_alter_listing_photo_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='property_age',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(limit_value=0)]),
            preserve_default=False,
        ),
    ]
