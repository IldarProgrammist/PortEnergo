from django.contrib import admin

# Register your models here.
from locations.models import Zone, Titul, Room


class TitulAdmin(admin.ModelAdmin):
    list_display = ['name', 'zone']

class RoomAdmin(admin.ModelAdmin):
    list_display = ['titul','name']


admin.site.register(Zone)
admin.site.register(Titul, TitulAdmin)
admin.site.register(Room, RoomAdmin)

