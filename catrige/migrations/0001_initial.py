# Generated by Django 3.0.8 on 2020-08-29 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Цвет')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Цвет',
                'verbose_name_plural': 'Цвета',
            },
        ),
        migrations.CreateModel(
            name='Firm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Фирма')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Фирма принтера',
                'verbose_name_plural': 'Фирмы принтеров',
            },
        ),
        migrations.CreateModel(
            name='PrinterStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Стаутс принтера')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Статус принтера',
                'verbose_name_plural': 'Статусы принтеров',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True, verbose_name='Статус')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Статус картриджа',
                'verbose_name_plural': 'Статусы картриджей',
            },
        ),
        migrations.CreateModel(
            name='PrinterModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Модель принтера')),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('slug', models.SlugField(unique=True)),
                ('firm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catrige.Firm', verbose_name='Фирма')),
            ],
            options={
                'verbose_name': 'Модель принтера',
                'verbose_name_plural': 'Модели принтеров',
            },
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=100, verbose_name='серийные номре')),
                ('ip', models.CharField(max_length=30, verbose_name='ip-адрес')),
                ('discription', models.TextField(blank=True, verbose_name='Описание')),
                ('printer_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catrige.PrinterModel', verbose_name='Модель принтера')),
                ('printer_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catrige.PrinterStatus', verbose_name='Статус принтера')),
            ],
            options={
                'verbose_name': 'Принтер',
                'verbose_name_plural': 'Принтеры',
            },
        ),
        migrations.CreateModel(
            name='CatrigeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название модели')),
                ('slug', models.SlugField(unique=True)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catrige.Color', verbose_name='Цвет')),
                ('printer_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catrige.PrinterModel', verbose_name='Модель принтера')),
            ],
            options={
                'verbose_name': 'Модель  картриджа',
                'verbose_name_plural': 'Модели картриджей',
            },
        ),
        migrations.CreateModel(
            name='Catrige',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serialNamber', models.CharField(max_length=30, verbose_name='Серийный номер')),
                ('date', models.DateField(auto_now_add=True)),
                ('catrige_models', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catrige.CatrigeModel', verbose_name='Модель картриджа')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catrige.Status', verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Картридж',
                'verbose_name_plural': 'Картриджи',
            },
        ),
    ]
