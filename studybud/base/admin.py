from django.contrib import admin
from .models import Room, Topic, Message

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'updated', 'created')
    list_filter = ('updated', 'created')
    search_fields = ('name', 'description')


class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'body', 'updated', 'created')
    list_filter = ('updated', 'created')
    search_fields = ('user__username', 'room__name', 'body')

admin.site.register(Room, RoomAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Message, MessageAdmin)
