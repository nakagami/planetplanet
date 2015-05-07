# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('link', models.CharField(max_length=1024)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=200, blank=True)),
                ('pub_dttm', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('rss_url', models.CharField(max_length=1024)),
                ('title', models.CharField(max_length=200, blank=True)),
                ('link', models.CharField(max_length=1024, blank=True)),
                ('subtitle', models.CharField(max_length=2048, blank=True)),
                ('author', models.CharField(max_length=200, blank=True)),
                ('pub_dttm_offset', models.IntegerField(default=0, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='feed',
            field=models.ForeignKey(to='planet.Feed'),
        ),
    ]
