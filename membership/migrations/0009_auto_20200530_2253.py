# Generated by Django 3.0.5 on 2020-05-30 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0008_auto_20200530_2231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='video',
        ),
        migrations.AddField(
            model_name='movie',
            name='video_url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
