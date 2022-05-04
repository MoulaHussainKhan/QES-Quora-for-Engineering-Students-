# Generated by Django 3.0.6 on 2020-05-24 05:58

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qnA', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='topics',
        ),
        migrations.AddField(
            model_name='question',
            name='topics',
            field=models.ManyToManyField(to='qnA.Topic'),
        ),
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.TextField(blank=True, max_length=4000),
        ),
        migrations.AlterField(
            model_name='question',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True),
        ),
    ]