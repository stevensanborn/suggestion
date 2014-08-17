from .models import UserProfile
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


class UserForm(forms.ModelForm):
	email = forms.EmailField(required=True)
	emailconfirm = forms.EmailField(required=True)
	password = forms.CharField(widget=forms.PasswordInput())
	passwordconfirm = forms.CharField(widget=forms.PasswordInput())
	def clean(self):
		if(self.cleaned_data.get('email') is not None):
			if ( self.cleaned_data.get('email').lower()!= self.cleaned_data.get('emailconfirm').lower()):
				self._errors['emailconfirm']=self.error_class(['Email addresses must match.'])
			elif(User.objects.filter(username=self.cleaned_data.get('email').lower()).exists()):
				self._errors['email']=self.error_class(['Email addresses already exists.'])
			elif ( self.cleaned_data.get('password').lower()!= self.cleaned_data.get('passwordconfirm').lower()):
				self._errors['password']=self.error_class(['Passwords do not match'])
			

		cleaned_data=super(UserForm, self).clean()
		
		return cleaned_data
	class Meta:
	    model = User
	    fields = ( 'email', 'emailconfirm', 'password','passwordconfirm')

class LoginForm(forms.ModelForm):
	email = forms.EmailField(required=True)
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
	    model = User
	    fields = ( 'email', 'password')

class AccountForm(forms.ModelForm):
	passwordold = forms.CharField(widget=forms.PasswordInput())
	password = forms.CharField(widget=forms.PasswordInput())
	passwordconfirm = forms.CharField(widget=forms.PasswordInput())
	class Meta:
	    model = User
	    fields = ( 'passwordold','password','passwordconfirm')

	