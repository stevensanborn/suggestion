from django.contrib import admin
from django.db import models
from .models import  Suggestion, Box , SuggestorType


class SuggestorTypeAdmin(admin.ModelAdmin):
	class Meta:
		model=SuggestorType

class BoxAdmin(admin.ModelAdmin):
	class Meta:
		model=Box

class SuggestionAdmin(admin.ModelAdmin):
	
	# readonly_fields = ('user',)
	class Meta:
		
		model=Suggestion

		def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
			
			field = super(SuggestionAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
       		
			if db_field.rel.to == User:
            
				field.label_from_instance = self.get_user_label
        	
			return field

admin.site.register(SuggestorType,SuggestorTypeAdmin)

admin.site.register(Suggestion,SuggestionAdmin)

admin.site.register(Box,BoxAdmin)