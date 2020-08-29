# Generated by Django 3.0.8 on 2020-08-23 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_auto_20200823_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='dep',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='person.Department', verbose_name='Отдел'),
            preserve_default=False,
        ),
    ]
