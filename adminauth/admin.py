from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Master,Designers

# Register your models here.
@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ['name','role','email','mobile','address','info','s_status']


@admin.register(Designers)
class DesignerAdmin(admin.ModelAdmin):
    list_display = ['name','number_of_pics','uplpics','desc','imgs']


