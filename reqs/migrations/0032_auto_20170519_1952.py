# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-19 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reqs', '0031_auto_20170519_1610'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequirementAllAgencies',
            fields=[
                ('id', models.CharField(max_length=1024, primary_key=True, serialize=False)),
            ],
            options={
                'managed': False,
                'db_table': 'reqs_requirement_all_agencies',
            },
        ),
        migrations.AlterModelOptions(
            name='agency',
            options={'ordering': ['name'], 'verbose_name': 'Agency', 'verbose_name_plural': 'Agencies'},
        ),
        migrations.AlterModelOptions(
            name='agencygroup',
            options={'ordering': ['name'], 'verbose_name': 'Agency Group', 'verbose_name_plural': 'Agency Groups'},
        ),
        migrations.AddField(
            model_name='requirement',
            name='all_agencies',
            field=models.ManyToManyField(related_name='all_requirements', through='reqs.RequirementAllAgencies', to='reqs.Agency'),
        ),
    ]