# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cts', '0002_auto_20150326_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='polygon',
            field=django.contrib.gis.db.models.fields.PolygonField(srid=4326, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='stable',
            field=models.ForeignKey(verbose_name=b'division', to='cts.Stable'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stable',
            name='polygon',
            field=django.contrib.gis.db.models.fields.PolygonField(srid=4326, null=True, blank=True),
            preserve_default=True,
        ),
    ]
