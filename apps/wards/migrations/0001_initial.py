# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ward_id', models.IntegerField()),
                ('ward_name', models.CharField(max_length=255)),
                ('tot_nm_hh', models.IntegerField(null=True, blank=True)),
                ('tot_pop', models.IntegerField(null=True, blank=True)),
                ('m_pop', models.IntegerField(null=True, blank=True)),
                ('f_pop', models.IntegerField(null=True, blank=True)),
                ('tot_l6', models.IntegerField(null=True, blank=True)),
                ('tot_sc', models.IntegerField(null=True, blank=True)),
                ('m_sc', models.IntegerField(null=True, blank=True)),
                ('f_sc', models.IntegerField(null=True, blank=True)),
                ('tot_st', models.IntegerField(null=True, blank=True)),
                ('m_st', models.IntegerField(null=True, blank=True)),
                ('f_st', models.IntegerField(null=True, blank=True)),
                ('tot_lit', models.IntegerField(null=True, blank=True)),
                ('m_lit', models.IntegerField(null=True, blank=True)),
                ('f_lit', models.IntegerField(null=True, blank=True)),
                ('tot_illt', models.IntegerField(null=True, blank=True)),
                ('f_illt', models.IntegerField(null=True, blank=True)),
                ('tot_w', models.IntegerField(null=True, blank=True)),
                ('m_w', models.IntegerField(null=True, blank=True)),
                ('f_w', models.IntegerField(null=True, blank=True)),
                ('tot_mnw', models.IntegerField(null=True, blank=True)),
                ('m_mnw', models.IntegerField(null=True, blank=True)),
                ('f_mnw', models.IntegerField(null=True, blank=True)),
                ('tot_cult', models.IntegerField(null=True, blank=True)),
                ('m_cult', models.IntegerField(null=True, blank=True)),
                ('f_cult', models.IntegerField(null=True, blank=True)),
                ('tot_aglb', models.IntegerField(null=True, blank=True)),
                ('m_aglb', models.IntegerField(null=True, blank=True)),
                ('f_aglb', models.IntegerField(null=True, blank=True)),
                ('tot_mfhh', models.IntegerField(null=True, blank=True)),
                ('m_mfhh', models.IntegerField(null=True, blank=True)),
                ('f_mfhh', models.IntegerField(null=True, blank=True)),
                ('tot_oth_w', models.IntegerField(null=True, blank=True)),
                ('m_other_w', models.IntegerField(null=True, blank=True)),
                ('f_other_w', models.IntegerField(null=True, blank=True)),
                ('tot_mrw', models.IntegerField(null=True, blank=True)),
                ('m_mrw', models.IntegerField(null=True, blank=True)),
                ('f_mrw', models.IntegerField(null=True, blank=True)),
                ('t_mrg_cult', models.IntegerField(null=True, blank=True)),
                ('m_mrg_cult', models.IntegerField(null=True, blank=True)),
                ('f_mrg_cult', models.IntegerField(null=True, blank=True)),
                ('t_mrg_aglb', models.IntegerField(null=True, blank=True)),
                ('m_mrg_aglb', models.IntegerField(null=True, blank=True)),
                ('f_mrg_aglb', models.IntegerField(null=True, blank=True)),
                ('t_mrg_hh', models.IntegerField(null=True, blank=True)),
                ('m_mrg_hh', models.IntegerField(null=True, blank=True)),
                ('f_mrg_hh', models.IntegerField(null=True, blank=True)),
                ('t_mrg_oth', models.IntegerField(null=True, blank=True)),
                ('m_mrg_oth', models.IntegerField(null=True, blank=True)),
                ('f_mrg_oth', models.IntegerField(null=True, blank=True)),
                ('tot_nnw', models.IntegerField(null=True, blank=True)),
                ('m_nnw', models.IntegerField(null=True, blank=True)),
                ('f_nnw', models.IntegerField(null=True, blank=True)),
                ('objectid', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
