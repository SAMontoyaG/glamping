from . import views
from django.urls import path

urlpatterns = [      
    path('', views.cabañas, name='cabañas'),  
    path('cabaña_status_/<int:cabaña_id>/', views.change_status_cabaña, name='cabaña_status'),            
          
]