# Generated by Django 4.0.4 on 2022-05-09 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actormovie',
            name='created_at',
        ),
    ]
