from django.contrib import messages
from django.conf import settings
from django.shortcuts import render,render_to_response, RequestContext, HttpResponseRedirect
from django.contrib.auth import authenticate, login , logout
from django.http import HttpResponseRedirect, HttpResponse
from django.db import models
from django.contrib.auth.models import User
from django.forms.util import ErrorList
from django.forms.forms import NON_FIELD_ERRORS
from django.core.urlresolvers import reverse
from django.core.mail import EmailMessage

import os

#from postmark import PMMail
from .forms import UserForm , LoginForm


# Create your views here.

def home(request):
	return  render_to_response("home.html",locals(),context_instance=RequestContext(request))



def thankyou(request):

	return  render_to_response("thankyou.html",locals(),context_instance=RequestContext(request))


def user_login(request):
	# Like before, obtain the context for the user's request.
	context = RequestContext(request)

	# If the request is a HTTP POST, try to pull out the relevant information.
	if request.method == 'POST':
		# Gather the username and password provided by the user.
		# This information is obtained from the login form.

		#validate the form
		form = LoginForm(request.POST)

		if(form.is_valid()) :

			email = request.POST['email'].lower()

			password = request.POST['password']

			# Use Django's machinery to attempt to see if the username/password
			# combination is valid - a User object is returned if it is.
			
			user = authenticate(username=email, password=password)

			# If we have a User object, the details are correct.
			# If None (Python's way of representing the absence of a value), no user
			# with matching credentials was found.

			if user:
			    # Is the account active? It could have been disabled.
			    if user.is_active:
			        # If the account is valid and active, we can log the user in.
			        # We'll send the user back to the homepage.
			        login(request, user)

			        return HttpResponseRedirect(reverse('account'))
			    else:
			        # An inactive account was used - no logging in!
			         form._errors[NON_FIELD_ERRORS] =form.error_class(['Your account is not enabled'])
			else:
			    # Bad login details were provided. So we can't log the user in.
			    form._errors[NON_FIELD_ERRORS] =form.error_class(['Invalid credentials'])

		return render_to_response('login.html', {'form':form}, context)

	# The request is not a HTTP POST, so display the login form.
	# This scenario would most likely be a HTTP GET.
	else:
		# No context variables to pass to the template system, hence the
		# blank dictionary object...
		return render_to_response('login.html', {}, context)

def get_started(request):
	# check if you are logged other wise go ro signup
	if request.user.is_authenticated():
		return HttpResponseRedirect("account")	
	else:
		return HttpResponseRedirect("signup")

def user_account(request):
	context = RequestContext(request)
	return render_to_response('account.html',{},context)

def user_signout(request):
	logout(request)
	return HttpResponseRedirect("/")

def register(request):
	# Like before, get the request's context.
	context = RequestContext(request)

	# A boolean value for telling the template whether the registration was successful.
	# Set to False initially. Code changes value to True when registration succeeds.
	registered = False

	# If it's a HTTP POST, we're interested in processing form data.
	if request.method == 'POST':
		# Attempt to grab information from the raw form information.
		# Note that we make use of both UserForm and UserProfileForm.
		user_form = UserForm(request.POST)
		
		# If the two forms are valid...
		if user_form.is_valid():
			# Save the user's form data to the database.
			
			user =  User(username=user_form.data['email'],email=user_form.data['email']);
			user.set_password(user_form.data['password'])

			# Now we hash the password with the set_password method.
			# Once hashed, we can update the user object.
			user.save()
			registered = True

			email = EmailMessage('Hello', 'World', to=['stevensanborn@gmail.com'])
			email.send()

			return HttpResponseRedirect('/')
		else:
			
			return render_to_response('registration.html',{'form': user_form},context)
			
	else:
		user_form = UserForm()
        
    
    	# Render the template depending on the context.
		return render_to_response('registration.html',{'form': user_form},context)