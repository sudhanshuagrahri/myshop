from django.urls import path, include
from . import views

app_name = 'adminauth'

urlpatterns = [
    path('',views.base,name='base'),
    path('manufacturers',views.manufacturers,name='manufacturers'),
    path('designers',views.designers,name='designers'),
    path('locate',views.locate,name='locate'),
]