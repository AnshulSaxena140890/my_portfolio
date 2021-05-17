from django.contrib import admin
from .models import *


# Register your models here.
class AdminContactDetails(admin.ModelAdmin):
    list_display = ['id', 'created_on', 'name', 'subject', 'email', 'is_active']
    list_filter = ['is_active']
    search_fields = ('id', 'email','name')


admin.site.register(ContactDetails, AdminContactDetails)