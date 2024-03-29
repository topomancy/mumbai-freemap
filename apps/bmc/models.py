from django.contrib.gis.db import models
import re

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
        verbose_name = 'MCGM Estates Leasehold Plot'

    def __unicode__(self):
        return self.lessee


class HolderHistory(models.Model):
    leasehold_plot = models.ForeignKey(LeaseholdPlot)
    text = models.TextField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.text


LEASE_BRANCH_CHOICES = (
    (1, 'I'),
    (2, 'II'),
    (3, 'III'),
    (4, 'IV'),
    (5, 'V'),
)

class EstateScheme(models.Model):
    name = models.CharField(max_length=255)
    scheme_number = models.IntegerField(blank=True, null=True)
    lease_branch = models.IntegerField(choices=LEASE_BRANCH_CHOICES, blank=True, null=True)
    declaration_date = models.DateField(blank=True, null=True)
    notification_date = models.DateField(blank=True, null=True)
    geometry = models.GeometryField(blank=True, null=True)
    scheme_map = models.URLField(blank=True, null=True)

    def no_of_plots(self):
        return self.leaseholdplot_set.count()

    def populate_scheme_number(self):
        name = self.name.strip()
        matches = re.findall(r'\d+$', name)
        if len(matches) > 0:
            number = matches[0]
            self.scheme_number = int(number)
            self.save()

    class Meta:
        verbose_name = 'MCGM Estates Scheme'
        ordering = ['scheme_number']

    def __unicode__(self):
        return self.name


class SchemeHistory(models.Model):
    estate_scheme = models.ForeignKey(EstateScheme)
    text = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)  

    def __unicode__(self):
        return self.text

    class Meta:
        verbose_name_plural = "Scheme Histories"


class VacantLandTenancy(models.Model):
    tenant = models.TextField()
    occupant = models.TextField()
    rent = models.CharField(max_length=256, blank=True, null=True)
    land_use = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    geometry = models.GeometryField(blank=True, null=True)

    def __unicode__(self):
        return self.tenant

    class Meta:
        verbose_name_plural = "Vacant Land Tenancies"