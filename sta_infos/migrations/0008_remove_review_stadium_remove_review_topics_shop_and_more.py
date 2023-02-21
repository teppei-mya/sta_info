# Generated by Django 4.1.5 on 2023-02-14 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sta_infos', '0007_alter_topic_stadium'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='stadium',
        ),
        migrations.RemoveField(
            model_name='review',
            name='topics',
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('lon', models.FloatField(null=True)),
                ('lat', models.FloatField(null=True)),
                ('website', models.CharField(max_length=200)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sta_infos.topic')),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='shop',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='sta_infos.shop'),
        ),
    ]