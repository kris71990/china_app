from django.contrib import admin

from .models import Region

class RegionAdmin(admin.ModelAdmin):
    list_display = ['region_name', 'region_type']


admin.site.register(Region, RegionAdmin)
