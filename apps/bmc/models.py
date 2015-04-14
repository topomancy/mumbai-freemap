from django.contrib.gis.db import models


class LeaseholdPlot(models.Model):
    lessee = models.CharField(max_length=512)
    cs_no = models.CharField(max_length=255, blank=True)
    value = models.IntegerField(blank=True, null=True)
    estate_scheme = models.ForeignKey("EstateScheme", blank=True, null=True)
    plot_no = models.CharField(max_length=255, blank=True, null=True)
    area = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    asset_no = models.IntegerField(blank=True, null=True)
    geometry = models.GeometryField(blank=True, null=True)

    def __unicode__(self):
        return self.lessee


class HolderHistory(models.Model):
    leasehold_plot = models.ForeignKey(LeaseholdPlot)
    text = models.TextField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.text


class EstateScheme(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


