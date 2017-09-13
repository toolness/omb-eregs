# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reqs', '0001_squashed_0040_auto_20170616_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='policy',
            name='managing_offices',
            field=models.ManyToManyField(blank=True, related_name='policies', to='reqs.Office'),
        ),
    ]