from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main),
    path('wind/', views.wind, name='wind'),
    path('fire/', views.fire, name='fire'),
    path('ice/', views.ice, name='ice'),
    path('lightning/', views.lightning, name='lightning')
]