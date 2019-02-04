# Generated by Django 2.1.5 on 2019-01-24 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogg', '0004_auto_20190124_0956'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadNum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reader_num', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='blog',
            name='reader_num',
        ),
        migrations.AddField(
            model_name='readnum',
            name='blog_count',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='blogg.Blog'),
        ),
    ]
