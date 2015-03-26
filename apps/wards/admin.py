from django.contrib.gis import admin
from models import *
from leaflet.admin import LeafletGeoAdmin

class WardAdmin(LeafletGeoAdmin):
    pass

admin.site.register(Ward, WardAdmin)