# Generated by Django 3.0.4 on 2020-05-07 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arts', '0005_films'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Films',
        ),
        migrations.DeleteModel(
            name='Games',
        ),
    ]
