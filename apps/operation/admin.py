from django.contrib import admin

from .models import UserMessage,UserFavorite,UserPassview
# Register your models here.

class UserMessageAdmin(admin.ModelAdmin):
    list_display = ["user","message","has_read","add_time"]  #显示的特征
    search_fields = ["user"]  #搜索的字段
    list_filter = ["user","has_read","add_time"] #过滤

class UserFavoriteAdmin(admin.ModelAdmin):
    list_display = ["user","fav_type","add_time"]  #显示的特征
    search_fields = ["user","fav_type"]  #搜索的字段
    list_filter = ["user","fav_type","add_time"] #过滤

class UserPassviewAdmin(admin.ModelAdmin):
    list_display = ["user","company","add_time"]  #显示的特征
    search_fields = ["user"]  #搜索的字段
    list_filter = ["user","add_time"] #过滤

admin.site.register(UserMessage,UserMessageAdmin)
admin.site.register(UserFavorite,UserFavoriteAdmin)
admin.site.register(UserPassview,UserPassviewAdmin)