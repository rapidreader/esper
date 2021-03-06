# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-12 12:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0003_show_hosts'),
    ]

    operations = [
        migrations.CreateModel(
            name='CanonicalShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('is_prime_time', models.BooleanField(default=False)),
                ('is_weekend', models.BooleanField(default=False)),
                ('is_recurring', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='show',
            name='canonical_show',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='query.CanonicalShow'),
        ),
    ]
