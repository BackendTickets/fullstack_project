# Generated by Django 4.2.2 on 2023-07-04 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_alter_movie_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
