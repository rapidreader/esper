# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-25 11:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0010_auto_20180625_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='face',
            name='bbox_score',
        ),
        migrations.RemoveField(
            model_name='object',
            name='bbox_score',
        ),
    ]
