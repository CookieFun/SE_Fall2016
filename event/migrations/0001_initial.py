# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-04 03:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='\u680f\u76ee\u540d')),
                ('slug', models.CharField(db_index=True, max_length=256, verbose_name='\u680f\u76ee\u7f51\u5740')),
                ('info', models.TextField(default='', verbose_name='\u680f\u76ee\u4fe1\u606f')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '\u680f\u76ee',
                'verbose_name_plural': '\u680f\u76ee',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='\u6807\u9898')),
                ('slug', models.CharField(db_index=True, max_length=256, verbose_name='\u7f51\u5740')),
                ('author', models.CharField(blank=True, max_length=256, verbose_name='\u4f5c\u8005')),
                ('content', models.TextField(blank=True, default='', verbose_name='\u5185\u5bb9')),
                ('column', models.ManyToManyField(to='event.Column', verbose_name='\u5f52\u5c5e\u680f\u76ee')),
            ],
            options={
                'verbose_name': '\u4e8b\u4ef6',
                'verbose_name_plural': '\u4e8b\u4ef6',
            },
        ),
    ]
