# Generated by Django 4.1.5 on 2023-02-13 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sta_infos', '0006_topic_stadium'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='stadium',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='sta_infos.stadium'),
        ),
    ]