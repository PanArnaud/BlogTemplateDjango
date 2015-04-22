# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150416_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60, verbose_name=b'Fichier')),
                ('image', models.FileField(upload_to=b'images/', verbose_name=b'Image')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Date de creation')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='photos',
            field=models.ManyToManyField(to='blog.Photo', null=True, blank=True),
        ),
    ]
