from django.contrib import admin

from bike.models import Bike, BikePart


class BikeAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'model', 'user', 'mileage']
    list_filter = ['name', ]
admin.site.register(Bike, BikeAdmin)


class BikePartAdmin(admin.ModelAdmin):
    list_display = ['name', 'type',  'user', 'mileage']
    list_filter = ['name', ]
admin.site.register(BikePart, BikePartAdmin)
