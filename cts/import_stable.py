#Usage:
# python manage.py shell
# import import_stable as i
# i.importStable(1, "Fort")

from cts.models import *
from os.path import join
import json
from django.conf import settings

JSON_DIR = settings.DATA_DIR

def importStables():
    for i in range(1,16):
        filename = join(JSON_DIR, "JSONforStable%d.json" % i)
        data = json.load(open(filename))
        stable_name = data[0]['division']
        s = Stable(stable_id=i, name=stable_name)
        s.save()
        for d in data:
            p = Property()
            for key in d.keys():
                val = d[key]
                if key in ['ground_rent_due', 'grant', 'total_due']:
                    if val == '':
                        val = 0.0
    #            if key in ['cs_no', 'cs_reg_no', 'cs_pg_no', 'cs_sheet_no']:
    #                if val == '' or val.find('..') != -1:
    #                    val = 0
                p.__setattr__(key, val)
            p.__setattr__('stable', s)
            p.save()
