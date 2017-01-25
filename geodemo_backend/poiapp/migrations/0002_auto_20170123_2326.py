# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-23 23:26
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('poiapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', verbose_name='slug')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='poi',
            options={'verbose_name_plural': 'Points of Interest'},
        ),
        migrations.AddField(
            model_name='poi',
            name='story',
            field=models.ManyToManyField(related_name='pois', to='poiapp.Story'),
        ),
    ]
