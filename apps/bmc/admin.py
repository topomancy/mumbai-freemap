from django.contrib import admin
from models import *
from leaflet.admin import LeafletGeoAdmin


class HolderHistoryInline(admin.StackedInline):
    model = HolderHistory


class LeaseholdPlotAdmin(LeafletGeoAdmin):
    search_fields = ('lessee', 'cs_no', 'estate_scheme__name', 'plot_no',)
    list_display = ('lessee', 'cs_no', 'plot_no', 'estate_scheme',)
    list_editable = ('cs_no', 'plot_no',)
    list_filter = ('estate_scheme',)
    inlines = [HolderHistoryInline]


class EstateSchemeAdmin(LeafletGeoAdmin):
    search_fields = ('name',)
    list_display = ('__unicode__', 'name', 'no_of_plots',)
    list_editable = ('name',)


admin.site.register(LeaseholdPlot, LeaseholdPlotAdmin)
admin.site.register(EstateScheme, EstateSchemeAdmin)
