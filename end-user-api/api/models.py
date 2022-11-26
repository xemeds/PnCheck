from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# Moved here from utils because of circular import
import string
import secrets

CHARACTERS = string.digits + string.ascii_uppercase + string.ascii_lowercase

def generate_key():
	while True:
		key = ''.join(secrets.choice(CHARACTERS) for i in range(32))

		if not API_Key.objects.filter(key=key):
			break

	return key

class API_Key(models.Model):
	key = models.CharField(max_length=32)
	last_called = models.DateTimeField(auto_now_add=True)

class User(AbstractUser):
	api_key = models.ForeignKey(API_Key, on_delete=models.CASCADE, null=True, blank=True)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_api_key(sender, instance=None, created=False, **kwargs):
	if created:
		api_key = API_Key(key=generate_key())
		api_key.save()
		instance.api_key = api_key
		instance.save()
