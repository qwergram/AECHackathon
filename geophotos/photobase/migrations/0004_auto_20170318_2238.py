# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 05:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photobase', '0003_auto_20170318_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='by',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
