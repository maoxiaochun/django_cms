# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0002_auto_20151019_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='column',
            name='home_display',
            field=models.BooleanField(verbose_name='首页显示', default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='column',
            name='nav_display',
            field=models.BooleanField(verbose_name='导航显示', default=False),
            preserve_default=True,
        ),
    ]
