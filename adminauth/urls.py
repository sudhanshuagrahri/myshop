from django.urls import path, include
from . import views

app_name = 'adminauth'

urlpatterns = [
    path('', views.masterpanel, name='masterpanel'),
    path('designers',views.designers,name='designers'),
    path('manufacturers',views.manufacturers,name='manufacturers'),

    path('des',views.des,name='des'),
    path('manu',views.manu,name='manu'),

    path('masterenroll',views.masterenroll,name='masterenroll'),


]