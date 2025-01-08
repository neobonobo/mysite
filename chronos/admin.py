from django.contrib import admin
from .models import ImportantDate

@admin.register(ImportantDate)
class ImportantDateAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time_since_display')
    search_fields = ('name', 'description')
    list_filter = ('date',)

    def time_since_display(self, obj):
        return obj.time_since()
    time_since_display.short_description = "Time Since"
