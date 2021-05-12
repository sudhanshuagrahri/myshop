from django.urls import path
from . import views

app_name = 'manufacturer'

urlpatterns = [
    path('orders/', views.show_order, name='show_order'),
    path('dispatch/<int:id>/', views.dispatch_order, name='dispatch_order'),
    path('add/', views.create_products, name='create_products'),
]