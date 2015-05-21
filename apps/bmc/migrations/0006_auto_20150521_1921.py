# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bmc', '0005_schemehistory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estatescheme',
            options={'ordering': ['scheme_number'], 'verbose_name': 'MCGM Estates Scheme'},
        ),
        migrations.AlterModelOptions(
            name='schemehistory',
            options={'verbose_name_plural': 'Scheme Histories'},
        ),
        migrations.AlterField(
            model_name='schemehistory',
            name='text',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
