# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-28 13:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network_name', models.CharField(max_length=30, unique=True, verbose_name='Network name')),
                ('ip', models.CharField(max_length=15, unique=True, verbose_name='Ip')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is active?')),
                ('datetime_connection', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Capture Date')),
            ],
            options={
                'verbose_name': 'Network',
                'verbose_name_plural': 'Networks',
            },
        ),
    ]
