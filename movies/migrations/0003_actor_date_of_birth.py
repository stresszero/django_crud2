# Generated by Django 4.0.4 on 2022-05-09 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_remove_actormovie_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]
