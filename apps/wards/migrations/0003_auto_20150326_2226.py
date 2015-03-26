# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wards', '0002_ward_geometry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ward',
            old_name='f_other_w',
            new_name='f_oth_w',
        ),
        migrations.RenameField(
            model_name='ward',
            old_name='m_other_w',
            new_name='m_oth_w',
        ),
    ]
