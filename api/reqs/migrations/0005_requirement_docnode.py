# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 16:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0001_initial'),
        ('reqs', '0004_remove_policy_managing_office'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirement',
            name='docnode',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='document.DocNode'),
        ),
    ]