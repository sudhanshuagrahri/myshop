from django.contrib import admin
from .models import Dispatch, ProductDetails

@admin.register(Dispatch)
class DispatchAdmin(admin.ModelAdmin):
    pass
    #list_display = ['order_id', 'sent_on', 'courier_no', 'delivered_on','exchange']
    #list_editable = ['sent_on', 'courier_no', 'delivered_on','exchange']
    
@admin.register(ProductDetails)
class ProductDetailsAdmin(admin.ModelAdmin):
    pass