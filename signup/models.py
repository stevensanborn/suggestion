from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)
	updated=models.DateTimeField(auto_now=False, auto_now_add=True)
	def __str__(self):
		return self.user.username


