# Generated by Django 3.0.5 on 2020-05-30 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0006_auto_20200530_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdb',
            field=models.FloatField(default=5),
        ),
    ]
