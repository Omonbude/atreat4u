from django.contrib import admin

# Register your models here.
<<<<<<< HEAD
from .models import ChangePasswordCode, CreateProfie
class ChangePasswordCodeAdmin(admin.ModelAdmin):
	fields = ['user_email', 'user_id']
	list_display = ['user_email', 'user_id']
admin.site.register(ChangePasswordCode, ChangePasswordCodeAdmin)
admin.site.register(CreateProfie)
=======
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
