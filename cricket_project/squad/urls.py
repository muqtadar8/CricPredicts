from django.urls import path
from . import views

urlpatterns = [
    path('squad/', views.getsquad, name='getsquad'),
    # path('onevsall/', views.onevsall, name='onevsall'),

    
    
]