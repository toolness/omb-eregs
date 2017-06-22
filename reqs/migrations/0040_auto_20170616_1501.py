# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-16 15:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    """Mass-create new revisions for each of the req models."""
    REVISED_MODELS = [
        ('reqs', 'Agency'),
        ('reqs', 'AgencyGroup'),
        ('reqs', 'Office'),
        ('reqs', 'Policy'),
        ('reqs', 'Requirement'),
        ('reqs', 'Topic'),
    ]

    dependencies = [
        ('reqs', '0039_merge_20170614_1333'),
    ]

    operations = [
    ]
