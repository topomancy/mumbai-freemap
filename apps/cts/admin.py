from django.contrib.gis import admin
# from django.contrib.gis.maps.google import GoogleMap
from models import *
from leaflet.admin import LeafletGeoAdmin


class PropertyAdmin(LeafletGeoAdmin):
    list_display = ('__unicode__', 'cs_no', 'cs_reg_no', 'street_locality', 'tenure', 'area_sqm',)
    list_filter = ('stable', 'cs_sheet_no',)
    search_fields = ('street_locality', 'division', 'cs_sheet_no', 'cs_no', 'holders_history',)
    # default_lon = 72.855211097628413
    # default_lat = 19.415775291486027
    # default_zoom = 4


admin.site.register(Property, PropertyAdmin)
admin.site.register(Stable)

