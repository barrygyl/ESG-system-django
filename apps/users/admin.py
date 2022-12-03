from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserProfile
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserProfile,UserAdmin)

admin.site.site_header = "ESG系统"
admin.site.site_title = "ESG系统"
admin.site.index_title = "ESG系统"