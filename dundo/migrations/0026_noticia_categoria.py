# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-24 23:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dundo', '0025_auto_20170525_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='noticias', to='dundo.Categoria'),
        ),
    ]