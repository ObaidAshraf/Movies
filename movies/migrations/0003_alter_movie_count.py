# Generated by Django 4.2.7 on 2023-11-18 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='count',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
