# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-10-19 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_addressbook_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='addressbook',
            name='company',
            field=models.CharField(blank=True, max_length=80, verbose_name='Company'),
        ),
    ]
