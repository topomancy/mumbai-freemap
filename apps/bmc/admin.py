from django.contrib import admin
from models import *
from leaflet.admin import LeafletGeoAdmin


class HolderHistoryInline(admin.StackedInline):
    model = HolderHistory


class SchemeHistoryInline(admin.StackedInline):
    model = SchemeHistory


class LeaseholdPlotAdmin(LeafletGeoAdmin):
    search_fields = ('lessee', 'cs_no', 'estate_scheme__name', 'plot_no',)
    list_display = ('lessee', 'cs_no', 'plot_no', 'estate_scheme',)
    list_editable = ('cs_no', 'plot_no',)
    list_filter = ('estate_scheme',)
    inlines = [HolderHistoryInline]


class EstateSchemeAdmin(LeafletGeoAdmin):
    inlines = [SchemeHistoryInline]
    search_fields = ('name',)
    list_display = ('__unicode__', 'scheme_number', 'name', 'no_of_plots',)
    list_editable = ('name',)


class VacantLandTenancyAdmin(LeafletGeoAdmin):
    search_fields = ('tenant', 'occupant', 'land_use', 'location',)
    list_display = ('tenant', 'occupant', 'land_use', 'rent', 'location',)
    list_filter = ('land_use',)

admin.site.register(LeaseholdPlot, LeaseholdPlotAdmin)
admin.site.register(EstateScheme, EstateSchemeAdmin)
admin.site.register(VacantLandTenancy, VacantLandTenancyAdmin)
