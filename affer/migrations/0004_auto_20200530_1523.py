# Generated by Django 3.0.4 on 2020-05-30 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affer', '0003_auto_20200530_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to='media'),
        ),
    ]
