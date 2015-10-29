# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='column',
            name='home_display',
        ),
        migrations.RemoveField(
            model_name='column',
            name='nav_display',
        ),
    ]
