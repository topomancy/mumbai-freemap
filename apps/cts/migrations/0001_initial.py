# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filename', models.CharField(max_length=255)),
                ('division', models.CharField(max_length=255)),
                ('cs_no', models.CharField(max_length=255)),
                ('cs_reg_no', models.CharField(max_length=255)),
                ('cs_pg_no', models.CharField(max_length=255, null=True, blank=True)),
                ('cs_sheet_no', models.CharField(max_length=255, null=True, blank=True)),
                ('street_locality', models.TextField(null=True, blank=True)),
                ('street_no', models.CharField(max_length=255, null=True, blank=True)),
                ('tenure', models.CharField(max_length=255, null=True, blank=True)),
                ('area_sqm', models.CharField(max_length=255, null=True, blank=True)),
                ('laughton_no', models.CharField(max_length=255, null=True, blank=True)),
                ('collector_new_no', models.CharField(max_length=255, null=True, blank=True)),
                ('collector_rent_no', models.CharField(max_length=255, null=True, blank=True)),
                ('ground_rent_due', models.FloatField(null=True, blank=True)),
                ('grant', models.FloatField(null=True, blank=True)),
                ('total_due', models.FloatField(null=True, blank=True)),
                ('holders_history', models.TextField(null=True, blank=True)),
                ('polygon', django.contrib.gis.db.models.fields.PolygonField(srid=4326, null=True)),
            ],
            options={
                'verbose_name_plural': 'Properties',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stable_id', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('polygon', django.contrib.gis.db.models.fields.PolygonField(srid=4326, null=True)),
            ],
            options={
                'ordering': ['stable_id'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='property',
            name='stable',
            field=models.ForeignKey(to='cts.Stable'),
            preserve_default=True,
        ),
    ]
