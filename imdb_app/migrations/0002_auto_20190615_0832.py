# Generated by Django 2.2.2 on 2019-06-15 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdb_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
