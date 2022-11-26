from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm):
		model = User
		fields = ('username',)

class CustomPasswordChangeForm(PasswordChangeForm):
	class Meta(PasswordChangeForm):
		model = User
		fields = ('username',)
