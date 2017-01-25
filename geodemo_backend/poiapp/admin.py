from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

from geodemo_backend.poiapp.models import Genre, Plugin, POI, Story


class POIAdmin(LeafletGeoAdmin):
    pass

# Register your models here.
admin.site.register(Genre)
admin.site.register(Plugin)
admin.site.register(POI, POIAdmin)
admin.site.register(Story)