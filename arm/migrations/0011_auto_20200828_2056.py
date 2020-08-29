# Generated by Django 3.0.8 on 2020-08-28 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arm', '0010_remove_pc_os'),
    ]

    operations = [
        migrations.AddField(
            model_name='pc',
            name='discription',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='pc',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='pc',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]