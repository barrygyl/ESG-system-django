# 人工智能
# 开发人：高云龙
# 开发时间：2022/9/25  15:01
from django import forms
from users.models import UserProfile
class LoginForm(forms.Form):
    Username = forms.CharField(required=True,min_length=2)
    Password = forms.CharField(required= True,min_length=3)

class RegisterPostForm(forms.Form):
    Username = forms.CharField(required=True, min_length=2)
    Password = forms.CharField(required=True, min_length=3)
    Nick_name = forms.CharField(required=True)
    Mobile = forms.CharField(required=True,max_length=11,min_length=11)
    def clean_username(self):
        Username = self.data.get("Username")
        users = UserProfile.objects.filter(Username = Username)
        if users:
            raise forms.ValidationError("用户已存在")
        return Username