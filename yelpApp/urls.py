from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('process', views.create),
    path('process2', views.login),
    path('login', views.log),
]