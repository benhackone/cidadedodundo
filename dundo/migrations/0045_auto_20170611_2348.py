# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-11 22:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dundo', '0044_emprego_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprego',
            name='icon',
        ),
        migrations.AddField(
            model_name='emprego',
            name='contactos',
            field=models.CharField(db_index=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='emprego',
            name='empresa',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='emprego',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='Emprego/%Y/%m/%d'),
        ),
    ]