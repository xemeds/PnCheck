from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

urlpatterns = [
    path('docs/', views.docs, name='api_docs'),
    path('key/', views.key, name='api_key'),

    path('login/',LoginView.as_view(template_name="api/login.html"),name="api_login"),
    path('register/',views.register,name="api_register"),
    path('change_password/',views.change_password,name="api_change_password"),
    path('logout/',LogoutView.as_view(template_name="api/logout.html"),name="api_logout"),
]
