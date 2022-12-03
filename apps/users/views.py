from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.urls import reverse

from users.models import UserProfile
from users.forms import LoginForm,RegisterPostForm
# Create your views here.

class LogoutView(View):
    def get(self,request,*args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse("index"))

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        return render(request,"register.html")

    def post(self, request, *args, **kwargs):
        register_post_form = RegisterPostForm(request.POST)
        if register_post_form.is_valid():
            user_name = register_post_form.cleaned_data["Username"]
            password = register_post_form.cleaned_data["Password"]
            mobile = register_post_form.cleaned_data["Mobile"]
            # 通过用户名查询用户是否存在
            user = UserProfile(username = user_name)
            user.set_password(password)
            user.mobile = mobile
            user.save()
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        else:
                # 查询到用户
                return render(request, "login1.html", {"msg": "用户存在"})




class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))
        return render(request,"login1.html")
    def post(self,request, *args, **kwargs):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data["Username"]
            password = login_form.cleaned_data["Password"]
            #通过用户密码查询用户是否存在
            user = authenticate(username=user_name,password = password)

            if user is not None:
                #查询到用户
                login(request,user)
                #登录成功后返回页面
                return HttpResponseRedirect(reverse("index"))
            else:
                #未查询到用户
                return render(request, "login1.html", {"msg": "用户名或密码错误"})
        else:
            return render(request, "login1.html", {"login_form": login_form})

