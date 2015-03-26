# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ward',
            name='geometry',
            field=django.contrib.gis.db.models.fields.PolygonField(srid=4326, null=True, blank=True),
            preserve_default=True,
        ),
    ]
