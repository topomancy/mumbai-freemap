# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cts', '0004_auto_20150414_1350'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'ordering': ['-cs_no'], 'verbose_name': 'City Survey Property Card'},
        ),
        migrations.AlterModelOptions(
            name='stable',
            options={'ordering': ['stable_id'], 'verbose_name': 'City Survey Division'},
        ),
    ]
