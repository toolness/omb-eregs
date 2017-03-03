# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 15:29
from __future__ import unicode_literals

import logging

from django.db import migrations
from django.db.models.aggregates import Count

logger = logging.getLogger(__name__)


def forward(apps, schema_editor):
    """Delete any duplicate req_ids"""
    Requirement = apps.get_model('reqs', 'Requirement')
    query = Requirement.objects.values_list('req_id').annotate(
        count=Count('req_id')).filter(count__gt=1).order_by('req_id')
    for req_id, count in query:
        logger.warning('Req Id %s appears %s times. Deleting extras.',
                       req_id, count)
        dupes = Requirement.objects.filter(req_id=req_id).order_by('pk')[1:]
        for dup in dupes:
            dup.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('reqs', '0014_auto_20170201_0006'),
    ]

    operations = [
        migrations.RunPython(forward, migrations.RunPython.noop)
    ]