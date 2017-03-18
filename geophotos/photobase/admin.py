from django.contrib import admin
from photobase.models import Location, Coords, SitePlan, SiteDoc, Image

# Register your models here.

admin.site.register(Location)
admin.site.register(Coords)
admin.site.register(SitePlan)
admin.site.register(SiteDoc)
admin.site.register(Image)