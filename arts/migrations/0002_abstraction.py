# Generated by Django 3.0.4 on 2020-05-06 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abstraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('thumb', models.ImageField(blank=True, default='default.png', upload_to='')),
            ],
        ),
    ]