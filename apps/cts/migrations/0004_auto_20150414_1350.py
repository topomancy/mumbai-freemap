# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cts', '0003_auto_20150326_2224'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'ordering': ['-cs_no'], 'verbose_name_plural': 'Properties'},
        ),
    ]
