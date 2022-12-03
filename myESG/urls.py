"""myESG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,register_converter,re_path
from django.views.generic import TemplateView
from users.views import LoginView, LogoutView, RegisterView
from company.views import CompanyView,CompanyPostView,CompanyPost_1View,ShowView
from django.views.static import serve
from myESG.settings import MEDIA_ROOT



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name = "index.html"),name = "index"),
    path('login1/', LoginView.as_view(), name = "login"),
    path('register/', RegisterView.as_view(), name="register"),
    path('servers/', CompanyPostView.as_view(), name="servers"),
    path('servers_1/', CompanyPost_1View.as_view(), name="servers_1"),
    path('logout/',LogoutView.as_view(),name = "logout"),
    #配置上传文件
    re_path(r'^media/(?P<path>.*)$',serve,{"document_root":MEDIA_ROOT}),
    #公司ESG信息
    path('company/', CompanyView.as_view(),name = "company"),
    #ESG数据可视化
    path('show/', ShowView.as_view(), name="show")
]
