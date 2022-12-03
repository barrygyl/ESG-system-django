from datetime import datetime

from django.db import models

from users.models import BaseModel
# Create your models here.
class City(BaseModel):
    name = models.CharField(max_length=20,verbose_name=u"城市名")
    desc = models.CharField(max_length=200,verbose_name=u"描述")

    class Meta:
        verbose_name = "城市"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=20,verbose_name=u"行业名")
    desc = models.CharField(max_length=200,verbose_name=u"描述")

    class Meta:
        verbose_name = "行业"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name


class Company(BaseModel):
    name = models.CharField(verbose_name="公司名称",max_length=100)
    desc = models.CharField(verbose_name="公司描述",max_length=300,blank=True,null=True)
    degree = models.CharField(max_length=5,verbose_name="ESG评分等级",choices=(("a","A"),("b","B"),("c","C"),("d","D"),("e","E"),("f","F")),blank=True,null=True)
    click_nums = models.IntegerField(default=0,verbose_name="点击数")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name=u"行业",blank=True,null=True)
    tag = models.CharField(verbose_name="公司标签",max_length=10,blank=True,null=True)
    detail = models.TextField(verbose_name="公司详情",blank=True,null=True)
    address = models.CharField(max_length=150,verbose_name="公司地址",blank=True,null=True)
    image = models.ImageField(upload_to="company/%Y/%m",verbose_name="封面图",max_length=100,blank=True,null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE,verbose_name=u"所在城市",blank=True,null=True)

    class Meta:
        verbose_name = "公司信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Company_E(BaseModel):
    company = models.ForeignKey(Company,verbose_name="公司", on_delete=models.CASCADE)
    name = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name=u"行业",blank=True,null=True)
    date = models.IntegerField(verbose_name="信息年份",max_length=4,default="2022")
    value = models.IntegerField(verbose_name="资产",default="0")
    Greenhouse_gas_emissions = models.IntegerField(verbose_name="温室气体排放量",default="0")
    Discharge_value_of_hazardous_waste = models.IntegerField(verbose_name="有害废弃物排放量",default="0")
    Discharge_value_of_harmless_waste = models.IntegerField(verbose_name="无害废弃物排放量",default="0")
    Energy_consumption = models.IntegerField(verbose_name="能源消耗量",default="0")
    water_consumption = models.IntegerField(verbose_name="耗水量",default="0")
    Environmental_protection_action_investment = models.IntegerField(verbose_name="环境保护投资量",default="0")

    class Meta:
        verbose_name = "公司环境信息"
        verbose_name_plural = verbose_name


class Company_S(BaseModel):
    company = models.ForeignKey(Company,verbose_name="公司", on_delete=models.CASCADE)
    name = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name=u"行业",blank=True,null=True)
    value = models.IntegerField(verbose_name="资产",default="0")

    class Meta:
        verbose_name = "公司社会信息"
        verbose_name_plural = verbose_name

class Company_G(BaseModel):
    company = models.ForeignKey(Company,verbose_name="公司", on_delete=models.CASCADE)
    name = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name=u"行业",blank=True,null=True)
    value = models.IntegerField(verbose_name="资产",default="0")
    class Meta:
        verbose_name = "公司管理信息"
        verbose_name_plural = verbose_name

class Company_E_Resource(BaseModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,verbose_name="名称")
    file = models.FileField(upload_to="course/resourse/%Y/%m",verbose_name="下载地址",max_length=200)

    class Meta:
        verbose_name = "公司E资源"
        verbose_name_plural = verbose_name

class Company_S_Resource(BaseModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="名称")
    file = models.FileField(upload_to="course/resourse/%Y/%m", verbose_name="下载地址", max_length=200)

    class Meta:
        verbose_name = "公司S资源"
        verbose_name_plural = verbose_name

class Company_G_Resource(BaseModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="名称")
    file = models.FileField(upload_to="course/resourse/%Y/%m", verbose_name="下载地址", max_length=200)

    class Meta:
        verbose_name = "公司G资源"
        verbose_name_plural = verbose_name

class Company_Resource(BaseModel):
    company = models.ForeignKey(Company, verbose_name="公司", on_delete=models.CASCADE)
    name = models.CharField(max_length=100,verbose_name="名称")
    file = models.FileField(upload_to="course/resourse/%Y/%m",verbose_name="下载地址",max_length=200)

    class Meta:
        verbose_name = "公司资源"
        verbose_name_plural = verbose_name