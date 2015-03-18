from django.contrib.gis.db import models

class Property(models.Model):
    filename = models.CharField(max_length=255)
    division = models.CharField(max_length=255)
    cs_no = models.CharField(max_length=255)
    cs_reg_no = models.CharField(max_length=255)
    cs_pg_no = models.CharField(max_length=255, blank=True, null=True)
    cs_sheet_no = models.CharField(max_length=255, blank=True, null=True)
    street_locality = models.TextField(blank=True, null=True)
    street_no = models.CharField(max_length=255, blank=True, null=True)
    tenure = models.CharField(max_length=255, blank=True, null=True)
    area_sqm = models.CharField(max_length=255, blank=True, null=True)
    laughton_no = models.CharField(max_length=255, blank=True, null=True)
    collector_new_no = models.CharField(max_length=255, blank=True, null=True)
    collector_rent_no = models.CharField(max_length=255, blank=True, null=True)
    ground_rent_due = models.FloatField(blank=True, null=True)
    grant = models.FloatField(blank=True, null=True)
    total_due = models.FloatField(blank=True, null=True)
    holders_history = models.TextField(blank=True, null=True)
    stable = models.ForeignKey("Stable")
    polygon = models.PolygonField(null=True)
    objects = models.GeoManager()

    def __unicode__(self):
        return "%s: %s" % (self.division, self.cs_no,)

    class Meta:
        verbose_name_plural = "Properties"


class Stable(models.Model):
    stable_id = models.IntegerField()
    name = models.CharField(max_length=255)
    polygon = models.PolygonField(null=True)
    objects = models.GeoManager()
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['stable_id']
