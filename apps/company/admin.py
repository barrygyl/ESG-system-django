from django.contrib import admin

from .models import Company,City,Company_E,Company_G,Company_S,Company_Resource,Category
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = [ "name", "desc", "city", "degree", "category"]
    list_per_page = 10
    search_fields = ["name","city", "degree", "category"]  #搜索的字段
    list_filter = ["name", "city", "degree", "category", "add_time"] #过滤

class CityAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "desc"]  #显示的特征
    search_fields = ["name"]  #搜索的字段
    list_filter = ["name", "add_time"] #过滤
    list_editable = ["name", "desc"]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "desc"]  #显示的特征
    search_fields = ["name"]  #搜索的字段
    list_filter = ["name", "add_time"] #过滤
    list_editable = ["name", "desc"]

class Company_EAdmin(admin.ModelAdmin):
    list_display = ["company", "name", "value"]  #显示的特征
    search_fields = ["name", "company"]  #搜索的字段
    list_filter = ["name", "add_time", "company__name"] #过滤

class Company_GAdmin(admin.ModelAdmin):
    list_display = ["company", "name", "value"] #显示的特征
    search_fields = ["name", "company"] #搜索的字段
    list_filter = ["name", "add_time", "company__name"] #过滤

class Company_SAdmin(admin.ModelAdmin):
    list_display = ["company", "name", "value"] #显示的特征
    search_fields = ["name", "company"] #搜索的字段
    list_filter = ["name", "add_time", "company__name"] #过滤

class Company_ResourceAdmin(admin.ModelAdmin):
    list_display = ["company", "name", "file"] #显示的特征
    search_fields = ["company"] #搜索的字段
    list_filter = ["name", "add_time", "company__name"] #过滤


admin.site.register(Company, CompanyAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Company_S, Company_SAdmin)
admin.site.register(Company_G, Company_GAdmin)
admin.site.register(Company_E, Company_EAdmin)
admin.site.register(Company_Resource, Company_ResourceAdmin)