import csv
from models import *
from os.path import join
from django.conf import settings
from decimal import Decimal


def get_decimal(val):
    val = val.strip()
    if val == '':
        return None
    return Decimal(val.replace(",", ""))

def do():
    file_path = join(settings.DATA_DIR, "bmc", "leasehold_plots.csv")
    reader = csv.reader(open(file_path))
    for row in reader:
        lp = LeaseholdPlot()
        lp.lessee = row[0]
        lp.cs_no = row[1]
        lp.holder_history_text = ''.join(row[2:25])
        lp.value = get_decimal(row[25])
        estate_scheme, created = EstateScheme.objects.get_or_create(name=row[26].strip())
        lp.estate_scheme = estate_scheme
        lp.plot_no = row[27]
        lp.area = get_decimal(row[28])
        lp.asset_no = int(row[29].strip())
        lp.save()
        print lp.lessee


def merge_estates():
    for e in EstateScheme.objects.distinct('name'):
        print e.name
        same_estates = EstateScheme.objects.filter(name=e.name).exclude(id=e.id)
        for s in same_estates:
            for plot in s.leaseholdplot_set.all():
                plot.estate_scheme = e
                plot.save()
            s.delete()


def remove_estates():
    for e in EstateScheme.objects.filter(name__contains='REMOVE'):
        e.delete()


