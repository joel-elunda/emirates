from django.contrib import admin
from room.models import RoomModel


@admin.register(RoomModel)
class RoomModelAdmin(admin.ModelAdmin):
    pass
