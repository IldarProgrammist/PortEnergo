# Generated by Django 3.0.8 on 2020-08-23 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0004_auto_20200823_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='date_add',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
