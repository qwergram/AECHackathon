from django.contrib import admin
from photobase.models import SiteDoc, Image, Project
from django.contrib.auth.models import User

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    search_fields = ['name', 'street', 'city', 'state', 'zip_code']
    list_display = ['name', 'street', 'city', 'state', 'zip_code']


admin.site.register(SiteDoc)
admin.site.register(Image)
admin.site.register(Project, ProjectAdmin)