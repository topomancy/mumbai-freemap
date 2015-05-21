# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bmc', '0004_auto_20150521_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchemeHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('estate_scheme', models.ForeignKey(to='bmc.EstateScheme')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
