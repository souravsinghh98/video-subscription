# Generated by Django 3.0.5 on 2020-06-01 10:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0013_usermembership_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermembership',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
    ]
