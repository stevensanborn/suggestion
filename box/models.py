from django.db import models
from django.contrib.auth.models import User
import uuid


class SuggestorType(models.Model):
	name=models.CharField(max_length=150, blank=False,unique=False)
	description=models.CharField(max_length=250, blank=False,unique=False)
	def __str__(self):
		return ("Type : "+self.name+" "+str(self.id))


class Box(models.Model):

	def _createHash():
		return str(uuid.uuid1())

	title=models.CharField(max_length=150, blank=False,unique=False)
	description=models.CharField(max_length=150, blank=False,unique=False)
	# name=models.CharField(max_length=250, blank=False,unique=False)
	suggestortype=models.ForeignKey(SuggestorType, default=1)
	#models.CharField(max_length=2,choices=SuggestorTypesChoices,default='AN')
	user = models.ForeignKey(User)
	timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)
	updated=models.DateTimeField(auto_now=False, auto_now_add=True)
	url_hash = models.CharField(default=_createHash, blank=False, max_length=50, unique=True)
    
	
	def __str__(self):
		return "Box :"+self.title


class Suggestion(models.Model):
	subject=models.CharField(max_length=150, blank=False,unique=False)
	txt=models.CharField(max_length=250, blank=False,unique=False)
	box=models.ForeignKey(Box)
	timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)
	updated=models.DateTimeField(auto_now=False, auto_now_add=True)
	# user = models.ForeignKey(User)
	def __str__(self):
		return self.txt+" "+str(self.id)