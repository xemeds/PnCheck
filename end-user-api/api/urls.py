from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="api_main"),
    path('predict', views.predict, name="api_predict"),
]
