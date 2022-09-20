from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 6

class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name',  'dealer_id', 'car_type', 'year']
    search_fields = ['name']

class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ['name', 'description']
    search_fields = ['name']

# Register models here

admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarMake)