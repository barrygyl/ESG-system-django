from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.urls import reverse

from company.models import Company,Company_E,Category
from myESG.settings import MEDIA_URL
from apps.company.forms import CompanyPostForm,CompanyPost_1Form
# Create your views here.

class CompanyView(View):
    def get(self,request,*args, **kwargs):
        #从数据库获取数据
        all_companys = Company.objects.all()
        companys_nums = Company.objects.count()
        return render(request, "company.html",{
            "all_companys":all_companys,
            "company_nums":companys_nums,
            })

class CompanyPostView(View):
    def get(self, request, *args, **kwargs):
        all_Categorys = Category.objects.all()
        return render(request,"servers.html",{
            "all_Categorys": all_Categorys,
        })

    def post(self, request, *args, **kwargs):
        company_post_form = CompanyPostForm(request.POST)
        if company_post_form.is_valid():
            name = company_post_form.cleaned_data["name"]
            category = request.POST.get('category')
            # 通过用户名查询用户是否存在
            new_name = name
            new_category = Category.objects.get(name = category)
            Company.objects.get_or_create(name=new_name,category =new_category)

            return HttpResponseRedirect(reverse("servers_1"))
        else:
                # 查询到公司
                return render(request, "server_1.html", {"msg": "公司存在"})



class ShowView(View):
    def get(self, request, *args, **kwargs):
        all_companys = Company.objects.all()
        companys_nums = Company.objects.count()
        companys_e = Company_E.objects.all()
        return render(request, "datashow.html",{
            "all_companys":all_companys,
            "company_nums":companys_nums,
            "companys_e":companys_e
            })


class CompanyPost_1View(View):
    def get(self, request, *args, **kwargs):
        all_companys = Company.objects.all()
        all_Categorys = Category.objects.all()
        return render(request,"servers_1.html",{
            "all_companys": all_companys,
            "all_Categorys": all_Categorys,
        })

    def post(self, request, *args, **kwargs):
        company_post_1_form = CompanyPost_1Form(request.POST)
        if company_post_1_form.is_valid():
            name = company_post_1_form.cleaned_data["name"]
            category = request.POST.get('category')
            date = company_post_1_form.cleaned_data["date"]

            company = Company.objects.get(name = name)
            e_name = Category.objects.get(name = category)
            e_date = date
            Company_E.objects.get_or_create(company=company,name =e_name,date=e_date)

            return HttpResponseRedirect(reverse("index"))
        else:
                # 查询到公司
                return render(request, "company.html", {"msg": "信息存在"})