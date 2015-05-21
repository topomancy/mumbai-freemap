# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bmc', '0003_auto_20150418_1123'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estatescheme',
            options={'verbose_name': 'MCGM Estates Scheme'},
        ),
        migrations.AlterModelOptions(
            name='leaseholdplot',
            options={'verbose_name': 'MCGM Estates Leasehold Plot'},
        ),
        migrations.AddField(
            model_name='estatescheme',
            name='declaration_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estatescheme',
            name='geometry',
            field=django.contrib.gis.db.models.fields.GeometryField(srid=4326, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estatescheme',
            name='lease_branch',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'I'), (2, b'II'), (3, b'III'), (4, b'IV'), (5, b'V')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estatescheme',
            name='notification_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estatescheme',
            name='scheme_map',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estatescheme',
            name='scheme_number',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
