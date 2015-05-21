# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bmc', '0006_auto_20150521_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='VacantLandTenancy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tenant', models.TextField()),
                ('occupant', models.TextField()),
                ('rent', models.CharField(max_length=256, null=True, blank=True)),
                ('land_use', models.CharField(max_length=256)),
                ('location', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name_plural': 'Vacant Land Tenancies',
            },
            bases=(models.Model,),
        ),
    ]
