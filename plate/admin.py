from django.contrib import admin
from plate.models import PlateModel


@admin.register(PlateModel)
class PlateModelAdmin(admin.ModelAdmin):
    pass