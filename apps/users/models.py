from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.
GENER_CHOICES = (
    ("male", "男"),
    ("female", "女")
)

class BaseModel(models.Model):
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        abstract = True

class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name='昵称',null=True, blank=True)
    birthday = models.DateField(verbose_name='生日', null=True,blank=True)
    denger = models.CharField(verbose_name="性别", choices=GENER_CHOICES,max_length=6)
    address = models.CharField(max_length=100, verbose_name="地址",default="")
    mobile = models.CharField(max_length=11, verbose_name="手机号码")
    image = models.ImageField(verbose_name="头像", upload_to="head_image/%y/%m", default="default.jpg")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.nick_name:
            return self.nick_name
        else:
            return self.username