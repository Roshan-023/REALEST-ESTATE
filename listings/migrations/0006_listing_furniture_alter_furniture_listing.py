# Generated by Django 4.2.7 on 2023-12-12 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_listing_furniture_type_furniture'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='furniture',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='listings_furniture', to='listings.furniture'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='furniture',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='furniture_items', to='listings.listing'),
        ),
    ]
