# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20150416_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='user',
        ),
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(default=1, verbose_name=b'Auteur', to=settings.AUTH_USER_MODEL),
        ),
    ]
