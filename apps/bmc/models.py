from django.contrib.gis.db import models


class LeaseholdPlot(models.Model):
    lessee = models.CharField(max_length=512)
    cs_no = models.CharField(max_length=255, blank=True)
    holder_history_text = models.TextField(blank=True)
    value = models.DecimalField(blank=True, null=True, max_digits=24, decimal_places=3)
    estate_scheme = models.ForeignKey("EstateScheme", blank=True, null=True)
    plot_no = models.CharField(max_length=255, blank=True, null=True)
    area = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    asset_no = models.IntegerField(blank=True, null=True)
    geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        verbose_name = 'MCGM Estates Leasehold Plots'

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

    def no_of_plots(self):
        return self.leaseholdplot_set.count()

    class Meta:
        verbose_name = 'MCGM Estates Scheme'

    def __unicode__(self):
        return self.name


