from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('one/', views.oneonone, name='oneonone'),
    path('onevsall/', views.onevsall, name='onevsall'),

    
    
]