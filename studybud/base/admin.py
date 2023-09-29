from django.contrib import admin
from .models import Room

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'updated', 'created')
    list_filter = ('updated', 'created')
    search_fields = ('name', 'description')

admin.site.register(Room, RoomAdmin)
