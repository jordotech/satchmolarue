# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-05-26 20:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='merge_parent',
            field=models.ForeignKey(blank=True, help_text=b'The contact object this one was merged into.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='merge_children', to='contact.Contact'),
        ),
    ]
