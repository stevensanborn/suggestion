from django.db import models




class Account(models.Model):
	email=models.EmailField(max_length=120, blank=False, null=False, unique=True)
	timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)
	updated=models.DateTimeField(auto_now=False, auto_now_add=True)
	def __str__(self):
		return  self.email.encode('utf-8')


class Box(models.Model):
	name=models.CharField(max_length=250, blank=False,unique=False)
	timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)
	updated=models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.name.encode('utf-8')


