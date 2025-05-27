from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import FreeClass

@admin.register(FreeClass)
class FreeClassAdmin(ImportExportModelAdmin):
    list_display = ('Block', 'Day', 'Time', 'Room_No', 'Floor', 'Room_Status', 'Room_Type', 'is_occupied',)
    list_display_links = ('Block',)
    search_fields = ('Block', 'Day', 'Time', 'is_occupied',)
    list_filter = ('Block', 'Day', 'Time', 'is_occupied', 'Floor')
