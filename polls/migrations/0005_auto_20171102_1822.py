# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 10:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20171102_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.BooleanField(default=True, verbose_name='状态'),
        ),
    ]
