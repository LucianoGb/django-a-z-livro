from django.contrib import admin
from .models import *

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'birthday', 'created_at', 'updated_at', 'token')
    

admin.site.register(Profile, ProfileAdmin)
