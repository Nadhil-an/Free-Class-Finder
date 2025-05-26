from django.contrib import admin
from . models import FreeClass
# Register your models here.

class FreeclassAdmin(admin.ModelAdmin):
    list_display = ('block','free_day','free_hour','room_status','room_type','is_occupied',)
    list_display_links = ('block',)
    search_fields = ('block','free_day','free_hour','is_occupied',)
    list_filter=('block','free_day','free_hour','is_occupied')

admin.site.register(FreeClass,FreeclassAdmin)
