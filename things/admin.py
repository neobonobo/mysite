from django.contrib import admin
from .models import Thing, ThingCategory

@admin.register(ThingCategory)
class ThingCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Thing)
class ThingAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'unit', 'value_per_unit')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)
    ordering = ('name',)
