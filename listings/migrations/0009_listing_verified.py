# Generated by Django 4.2.7 on 2023-12-12 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_remove_listing_furniture_delete_furniture'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]