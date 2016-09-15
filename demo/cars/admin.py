from django.contrib import admin
from cars.models import Car,UserProfile

# Register your models here.


class CarAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'manufacturer', 'price', 'mileage', ]

admin.site.register(Car, CarAdmin)
admin.site.register(UserProfile)
