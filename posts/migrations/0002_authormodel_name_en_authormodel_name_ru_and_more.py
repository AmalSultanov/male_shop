# Generated by Django 4.1.2 on 2022-10-29 10:02

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authormodel',
            name='name_en',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='authormodel',
            name='name_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='title_en',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='title_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='content_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='content_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='title_en',
            field=models.CharField(max_length=512, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='title_ru',
            field=models.CharField(max_length=512, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='posttagmodel',
            name='title_en',
            field=models.CharField(max_length=20, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='posttagmodel',
            name='title_ru',
            field=models.CharField(max_length=20, null=True, verbose_name='title'),
        ),
    ]
