from django.shortcuts import render,render_to_response, RequestContext
from .forms import AccountForm

# Create your views here.

def home(request):

	form = AccountForm(request.POST or None)

	if form.is_valid():
		save_it=form.save(commit=False)
		save_it.save()

	return  render_to_response("signup.html",locals(),context_instance=RequestContext(request))