from django.contrib import admin
from .models import Person, SCategory, PromoCode, RefearlCode

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['gender', 'phone_no', 'grp', 'address', 'info']
    
@admin.register(SCategory)
class SCategoryAdmin(admin.ModelAdmin):
    list_display = ['subcategory']

@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ['name', 'typeOfOrg', 'promocode', 'percentageOfDis', 'validUpto', 'info']

@admin.register(RefearlCode)
class RefearlCodeAdmin(admin.ModelAdmin):
    list_display = ['name', 'typeOf', 'code', 'points', 'validUpto', 'info']    