from django import forms
from .models import Box,Suggestion,SuggestorType


class BoxForm(forms.Form):
	title=forms.CharField(max_length=150)
	description=forms.CharField(max_length=150)
	suggestortype=forms.ChoiceField(choices= [ (o.id, o.name) for o in SuggestorType.objects.all()] ,widget=forms.RadioSelect)

	class Meta:
		model = Box
		fields = ( 'title','description','suggestortype')



class OpenSuggestionForm(forms.Form):
	subject=forms.CharField(max_length=150)
	txt=forms.CharField(max_length=150)
	
	class Meta:
		model = Suggestion
		fields = ( 'subject','txt')
#usertype=forms.ModelMultipleChoiceField(queryset=.objects.all())