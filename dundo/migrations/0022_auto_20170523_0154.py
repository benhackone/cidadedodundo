# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-23 00:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dundo', '0021_auto_20170523_0151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noticia',
            old_name='status',
            new_name='estado',
        ),
    ]
