# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-31 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawling', '0002_auto_20181031_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
