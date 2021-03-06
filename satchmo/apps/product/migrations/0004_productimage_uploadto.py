# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-07-06 14:57
from __future__ import unicode_literals

from django.db import migrations
import product.models
import satchmo_utils.thumbnail.field


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_longer_key_pricelookup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='picture',
            field=satchmo_utils.thumbnail.field.ImageWithThumbnailField(max_length=200, upload_to=product.models.product_image_directory_path),
        ),
    ]
