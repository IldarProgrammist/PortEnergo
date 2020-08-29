# Generated by Django 3.0.8 on 2020-08-29 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Название зоны')),
            ],
            options={
                'verbose_name': 'Зона',
                'verbose_name_plural': 'Зоны',
            },
        ),
    ]