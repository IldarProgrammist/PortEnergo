# Generated by Django 3.0.8 on 2020-08-28 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arm', '0006_auto_20200828_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pc',
            name='name',
        ),
    ]