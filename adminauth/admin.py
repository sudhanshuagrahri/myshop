from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Master,Manufacturers,Designers

# Register your models here.
@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ['name','role','email']

@admin.register(Manufacturers)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name','Qty','Courier_number','comments']

@admin.register(Designers)
class DesignerAdmin(admin.ModelAdmin):
    list_display = ['name','product_code','nop','uplpics','desc','price']