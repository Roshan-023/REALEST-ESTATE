# Generated by Django 4.2.7 on 2023-12-13 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_useraccount_is_active_useraccount_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/'),
        ),
    ]