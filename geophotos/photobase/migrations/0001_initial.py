# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 20:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('x', models.DecimalField(decimal_places=16, max_digits=21)),
                ('y', models.DecimalField(decimal_places=16, max_digits=21)),
                ('floor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='media/dcim/')),
                ('note', models.TextField()),
                ('flag', models.IntegerField()),
                ('by', models.ManyToManyField(related_name='images', to=settings.AUTH_USER_MODEL)),
                ('geo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photobase.Coords')),
                ('tags', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('house_number', models.IntegerField()),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=2)),
                ('zip_code', models.IntegerField()),
                ('by', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SiteDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('by', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photobase.Location')),
            ],
        ),
        migrations.CreateModel(
            name='SitePlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('external', models.CharField(max_length=255, unique=True)),
                ('image', models.ImageField(upload_to='media/sites/')),
                ('by', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='sitedoc',
            name='site_plan',
            field=models.ManyToManyField(to='photobase.SitePlan'),
        ),
        migrations.AddField(
            model_name='coords',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photobase.Location'),
        ),
        migrations.AddField(
            model_name='coords',
            name='by',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
