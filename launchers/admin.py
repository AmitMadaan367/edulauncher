from django.contrib import admin


# Register your models here.

from .models import *
admin.site.register(LoginHistory)
admin.site.register(break_times)
admin.site.register(idinfo)
admin.site.register(Followup)
admin.site.register(FileNote)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ['userid','first_name','last_name','Gender','contact_number','Email']

admin.site.register(User_Profile)
admin.site.register(country)

@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
	list_display = ['userid']