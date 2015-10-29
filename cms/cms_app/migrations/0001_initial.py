# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='标题', max_length=256)),
                ('slug', models.CharField(verbose_name='网址', db_index=True, max_length=256)),
                ('content', DjangoUeditor.models.UEditorField(verbose_name='内容', blank=True, default='')),
                ('published', models.BooleanField(verbose_name='正式发布', default=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True, null=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, verbose_name='作者', null=True)),
            ],
            options={
                'verbose_name': '新闻',
                'verbose_name_plural': '新闻',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='栏目名称', max_length=256)),
                ('slug', models.CharField(verbose_name='栏目网址', db_index=True, max_length=256)),
                ('intro', models.TextField(verbose_name='栏目简介', default='')),
                ('nav_display', models.BooleanField(verbose_name='导航显示', default=False)),
                ('home_display', models.BooleanField(verbose_name='首页显示', default=False)),
            ],
            options={
                'verbose_name': '栏目',
                'verbose_name_plural': '栏目',
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='column',
            field=models.ManyToManyField(verbose_name='归属栏目', to='cms_app.Column'),
            preserve_default=True,
        ),
    ]
