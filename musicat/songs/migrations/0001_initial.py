# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-21 10:42
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import songs.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100, unique=True)),
                ('genre', models.TextField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(max_length=30)),
                ('image', models.ImageField(upload_to='group_photos')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=songs.models.get_slug, unique=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs.Group')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]