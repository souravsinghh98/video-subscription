# Generated by Django 3.0.5 on 2020-06-01 10:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0012_auto_20200531_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermembership',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
