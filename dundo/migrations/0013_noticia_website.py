# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-22 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dundo', '0012_auto_20170523_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]
