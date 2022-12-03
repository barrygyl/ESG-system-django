# 人工智能
# 开发人：高云龙
# 开发时间：2022/9/26  18:28

from django import forms

from company.models import Company,Company_G,Company_S,Company_E


class CompanyPostForm(forms.Form):
    name = forms.CharField(required=True, min_length=1)

    def clean_username(self):
        name = self.data.get("name")
        companys = Company.objects.filter(name = name)
        if companys:
            raise forms.ValidationError("公司已存在")
        return name

class CompanyPost_1Form(forms.Form):
    company = forms.CharField(required=True, min_length=1)
    date = forms.IntegerField(required=True,min_value=4,max_value=4)

    def clean_company_e(self):
        company = self.data.get("company")
        date = self.data.get("date")
        companys_e = Company_E.objects.filter(company = company,date = date)

        if companys_e:
            raise forms.ValidationError("信息已存在")
        return company,date