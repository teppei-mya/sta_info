# Generated by Django 4.1.5 on 2023-02-15 05:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sta_infos', '0008_remove_review_stadium_remove_review_topics_shop_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
