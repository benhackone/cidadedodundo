# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-12 18:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dundo', '0046_eventos'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categoria',
            new_name='CategoriaNoticia',
        ),
        migrations.AlterModelOptions(
            name='categoriaemprego',
            options={'ordering': ('nome',), 'verbose_name': 'categoriaEmprego', 'verbose_name_plural': 'categoriasEmprego'},
        ),
        migrations.AlterModelOptions(
            name='categorianoticia',
            options={'ordering': ('nome',), 'verbose_name': 'categoria_noticia', 'verbose_name_plural': 'categoriasNoticia'},
        ),
        migrations.RenameField(
            model_name='emprego',
            old_name='categoria',
            new_name='categoria_emprego',
        ),
        migrations.RenameField(
            model_name='noticia',
            old_name='categoria',
            new_name='categoria_noticia',
        ),
    ]