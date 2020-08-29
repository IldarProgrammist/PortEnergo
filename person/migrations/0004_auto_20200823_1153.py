# Generated by Django 3.0.8 on 2020-08-23 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_person_dep'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='dep',
        ),
        migrations.AddField(
            model_name='person',
            name='pos',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='person.Position', verbose_name='Должность'),
            preserve_default=False,
        ),
    ]