from django.urls import path
from .views import outlet_list, search_outlets

urlpatterns = [
    path('outlets/', outlet_list, name='outlet-list'),  
    path('outlets/search/', search_outlets, name='outlet-search'),  
]