# Generated by Django 4.1.5 on 2023-02-21 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sta_infos', '0011_remove_shop_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='distance',
            field=models.IntegerField(default=0),
        ),
    ]
