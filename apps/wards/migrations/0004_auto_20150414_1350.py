# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wards', '0003_auto_20150326_2226'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ward',
            options={'verbose_name': 'Greater Mumbai Administrative Ward', 'verbose_name_plural': 'Greater Mumbai Administrative Wards'},
        ),
    ]
