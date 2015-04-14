# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EstateScheme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HolderHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LeaseholdPlot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lessee', models.CharField(max_length=512)),
                ('cs_no', models.CharField(max_length=255, blank=True)),
                ('value', models.IntegerField(null=True, blank=True)),
                ('plot_no', models.CharField(max_length=255, null=True, blank=True)),
                ('area', models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True)),
                ('asset_no', models.IntegerField(null=True, blank=True)),
                ('geometry', django.contrib.gis.db.models.fields.GeometryField(srid=4326, null=True, blank=True)),
                ('estate_scheme', models.ForeignKey(blank=True, to='bmc.EstateScheme', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='holderhistory',
            name='leasehold_plot',
            field=models.ForeignKey(to='bmc.LeaseholdPlot'),
            preserve_default=True,
        ),
    ]
