# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bmc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaseholdplot',
            name='holder_history_text',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
