# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-04 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0002_auto_20180529_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='hosts',
            field=models.ManyToManyField(blank=True, to='query.Thing'),
        ),
    ]
