# Generated by Django 4.1.5 on 2023-02-13 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sta_infos', '0005_remove_review_review_remove_topic_stadium_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='stadium',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sta_infos.stadium'),
        ),
    ]
