from django.contrib import admin
from models import *
from leaflet.admin import LeafletGeoAdmin


class HolderHistoryInline(admin.StackedInline):
    model = HolderHistory


class LeaseholdPlotAdmin(LeafletGeoAdmin):
    search_fields = ('lessee', 'cs_no', 'estate_scheme__name', 'asset_no',)
    list_display = ('lessee', 'cs_no', 'estate_scheme', 'asset_no',)
    list_filter = ('estate_scheme',)
    inlines = [HolderHistoryInline]


class EstateSchemeAdmin(LeafletGeoAdmin):
    search_fields = ('name',)


admin.site.register(LeaseholdPlot, LeaseholdPlotAdmin)
admin.site.register(EstateScheme, EstateSchemeAdmin)
