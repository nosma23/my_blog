# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-06 12:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20160904_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='user',
        ),
        migrations.DeleteModel(
            name='Newsletter',
        ),
    ]
