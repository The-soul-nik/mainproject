# Generated by Django 3.0.4 on 2020-05-30 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affer', '0002_tag_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
