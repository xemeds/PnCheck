from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main_index'),
    path('info/', views.info, name='main_info'),
]
