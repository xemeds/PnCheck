from django.contrib import admin
from .models import API_Key, User

admin.site.register(User)
admin.site.register(API_Key)
