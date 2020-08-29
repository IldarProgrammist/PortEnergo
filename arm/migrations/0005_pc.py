# Generated by Django 3.0.8 on 2020-08-28 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arm', '0004_auto_20200828_2017'),
    ]

    operations = [
        migrations.CreateModel(
            name='PC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serialNamber', models.CharField(max_length=50, verbose_name='Серийный номер')),
                ('catregory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arm.Category', verbose_name='Категория')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arm.Model', verbose_name='Модель')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
