# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-25 13:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ebook', '0003_auto_20160724_1454'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Language',
            new_name='Idioma',
        ),
    ]
