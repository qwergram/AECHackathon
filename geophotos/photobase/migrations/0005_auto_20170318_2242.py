# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 05:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photobase', '0004_auto_20170318_2238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='by',
        ),
        migrations.RemoveField(
            model_name='project',
            name='by',
        ),
        migrations.RemoveField(
            model_name='sitedoc',
            name='by',
        ),
    ]
