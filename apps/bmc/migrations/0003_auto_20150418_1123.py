# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bmc', '0002_leaseholdplot_holder_history_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaseholdplot',
            name='value',
            field=models.DecimalField(null=True, max_digits=24, decimal_places=3, blank=True),
            preserve_default=True,
        ),
    ]
