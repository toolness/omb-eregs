# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 16:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    # trigger generation of new revisions
    REVISED_MODELS = [('reqs', 'Policy')]

    dependencies = [
        ('reqs', '0003_auto_20170913_1544'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='policy',
            name='managing_office',
        ),
    ]
