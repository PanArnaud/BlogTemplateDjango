# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150416_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='photos',
            field=models.ImageField(upload_to=b'images/', null=True, verbose_name=b'Image(s)', blank=True),
        ),
    ]
