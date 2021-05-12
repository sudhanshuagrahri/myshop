from django.contrib import admin
from .models import Order, OrderItem, OrderCustItem, Pincode


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

@admin.register(OrderCustItem)
class OrderCustAdmin(admin.ModelAdmin):
    list_display = ['id','order','product']

@admin.register(Pincode)
class PincodeAdmin(admin.ModelAdmin):
    list_display = ['city', 'pincode', 'hasCOD', 'hasPrepaid']