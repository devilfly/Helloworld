# Generated by Django 2.1.5 on 2019-01-24 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogg', '0005_auto_20190124_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='readnum',
            name='blog_count',
        ),
        migrations.DeleteModel(
            name='ReadNum',
        ),
    ]