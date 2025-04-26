from django.contrib import admin
from .models import Theatre, Show

@admin.register(Theatre)
class TheatreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')

@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ('movie', 'theatre', 'start_time', 'language')
    list_filter = ('theatre', 'language', 'start_time')
    search_fields = ('movie__title', 'theatre__name')
