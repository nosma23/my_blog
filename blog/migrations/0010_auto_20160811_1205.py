# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-11 12:05
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20160811_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
