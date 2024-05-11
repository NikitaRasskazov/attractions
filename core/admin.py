from django.contrib import admin

from core import models

@admin.register(models.Attractions)
class Attractions(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(models.AttractionImage)
class AttractionImage(admin.ModelAdmin):
    list_display = ('id', 'attraction')
