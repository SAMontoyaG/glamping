from . import views
from django.urls import path

urlpatterns = [      
    path('', views.hospedajes, name='hospedajes'),            
    path('hospedaje_status_/<int:hospedaje_id>/', views.change_status_hospedaje, name='hospedaje_status'),
]