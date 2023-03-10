# Generated by Django 4.1.2 on 2022-10-29 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannermodel',
            name='description_en',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='bannermodel',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='bannermodel',
            name='first_title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='first_title'),
        ),
        migrations.AddField(
            model_name='bannermodel',
            name='first_title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='first_title'),
        ),
        migrations.AddField(
            model_name='bannermodel',
            name='second_title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='second_title'),
        ),
        migrations.AddField(
            model_name='bannermodel',
            name='second_title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='second_title'),
        ),
    ]
