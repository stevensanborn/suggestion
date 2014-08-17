import os

from django.contrib import messages
from django.conf import settings
from django.shortcuts import render,render_to_response, RequestContext, HttpResponseRedirect
from django.contrib.auth import authenticate, login , logout
from django.http import HttpResponseRedirect, HttpResponse
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Min, Sum, Avg

from .forms import BoxForm,OpenSuggestionForm
from .models import Box,SuggestorType,Suggestion


def open_box(request,url_hash):
	B=Box.objects.get(url_hash=url_hash)
	if request.method == 'POST':
		print("POST")
		form=OpenSuggestionForm(request.POST)
		if form.is_valid():
			S=Suggestion(txt=form.data['txt'],subject=form.data['subject'],box=B)
			S.save()
			return HttpResponseRedirect('/suggestion/'+B.url_hash+'/thankyou')
	else:
		form=OpenSuggestionForm()		
	return render_to_response('open-suggestion-box.html', {'Box':B,'request':request,'form':form},context_instance=RequestContext(request))


def open_box_thankyou(request,url_hash):
	B=Box.objects.get(url_hash=url_hash)
	return render_to_response('open-suggestion-box-thankyou.html', {'Box':B,'request':request},context_instance=RequestContext(request))

def user_box(request,box_id):
	B=Box.objects.get(id=box_id)
	SList= Suggestion.objects.filter(box=B)
	return render_to_response('suggestion-box.html', {'Box':B,'Suggestions':SList,'request':request},context_instance=RequestContext(request))

@login_required
def user_home(request):
	BList=Box.objects.filter(user=request.user).annotate(Count('suggestion'))
	return render_to_response('account.html', {'Boxes':BList},context_instance=RequestContext(request))

@login_required
def user_boxes(request):
	BList=Box.objects.filter(user=request.user).annotate(Count('suggestion'))
	return render_to_response('suggestion-boxes.html', {'Boxes':BList},context_instance=RequestContext(request))

@login_required
def user_boxes_create(request):
	if request.method == 'POST':
		
		form=BoxForm(request.POST)

		if form.is_valid():

			B =  Box(title=form.data['title'],description=form.data['description'],suggestortype=SuggestorType.objects.filter(id=form.data['suggestortype'])[0],user=request.user);
			B.save()
			print("Saved boX")	
			return HttpResponseRedirect('/account/suggestion-boxes/')


	else:
		form=BoxForm()	
		
	return render_to_response('suggestion-boxes-create.html', {'form': form},context_instance=RequestContext(request))

