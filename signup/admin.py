from django.contrib import admin

# Register your models here.


from .models import Account

class AccountAdmin(admin.ModelAdmin):
	class Meta:
		model=Account


admin.site.register(Account,AccountAdmin)