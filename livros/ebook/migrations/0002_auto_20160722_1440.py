# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-22 14:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ebook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='publication_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]