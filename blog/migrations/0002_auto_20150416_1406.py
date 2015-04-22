# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='user',
            field=models.ForeignKey(default=1, verbose_name=b'Utilisateur', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(verbose_name=b'Contenu'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(verbose_name=b'Categorie', to='blog.Category'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateField(auto_now_add=True, verbose_name=b'Date de creation', db_index=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(unique=True, max_length=100, verbose_name=b'Slug'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(unique=True, max_length=100, verbose_name=b'Titre'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100, verbose_name=b'Slug'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=100, verbose_name=b'Titre', db_index=True),
        ),
    ]
