# Generated by Django 3.0.5 on 2020-05-30 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0005_auto_20200530_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('Hollywood', 'holly'), ('Bollywood', 'bolly'), ('Dual audio', 'dual'), ('Uncategorized', 'uncategorized')], default='Uncategorized', max_length=20),
        ),
        migrations.AddField(
            model_name='movie',
            name='imdb',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='movie',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='movie',
            name='video',
            field=models.FileField(null=True, upload_to='media/movies'),
        ),
        migrations.DeleteModel(
            name='ViewMovie',
        ),
    ]
