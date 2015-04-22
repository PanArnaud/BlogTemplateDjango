# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150416_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='photos',
        ),
        migrations.AddField(
            model_name='blog',
            name='photos',
            field=models.FileField(upload_to=b'images/', null=True, verbose_name=b'Image', blank=True),
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
