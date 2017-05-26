# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-14 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dundo', '0007_noticia_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='image',
            field=models.FileField(blank=True, upload_to='noticia/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='noticia_texto',
            field=models.TextField(max_length=9000),
        ),
    ]