# Generated by Django 3.0.5 on 2020-06-01 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0014_auto_20200601_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermembership',
            name='membership',
            field=models.ForeignKey(default='Free', null=True, on_delete=django.db.models.deletion.SET_NULL, to='membership.Membership'),
        ),
    ]
