# Generated by Django 2.1.5 on 2019-01-24 09:56

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogg', '0003_auto_20190123_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='reader_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
