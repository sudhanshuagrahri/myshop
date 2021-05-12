from django.urls import path, include
from . import views

app_name='designer'

urlpatterns = [
    path('list/', views.manufacturer_list, name="manufacturer_list"),
    path('list/<int:pk>', views.manufacturer_detail, name="manufacturer_detail"),
    path('list/manufactur_products_list/<int:pk>', views.manufacturer_products, name="manufactur_products_list"),
    path('list/manufactur_product_approved/<int:id>', views.product_approved, name="manufactur_product_approved"),
    path('list/manufactur_product_decline/<int:id>', views.product_decline, name="manufactur_product_decline"),
]