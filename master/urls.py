from django.urls import path
from . import views

app_name = 'master'

urlpatterns = [
    path('register/', views.registerPerson, name='registerPerson'),
    path('addpromo/', views.addPC, name='addPC'),
    path('addrefearl/', views.addRC, name='addRC'),
]