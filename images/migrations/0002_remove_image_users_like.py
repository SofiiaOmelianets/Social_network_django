# Generated by Django 3.0.4 on 2020-04-01 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='users_like',
        ),
    ]