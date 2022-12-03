from django.db import models

from django.contrib.auth import get_user_model

from users.models import BaseModel
from company.models import Company

# Create your models here.
UserProfile = get_user_model()

class UserFavorite(BaseModel):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name="用户")
    fav_id = models.IntegerField(verbose_name="数据id")
    fav_type = models.IntegerField(choices=((1,"公司"),(2,"ESG")),default=1,verbose_name="收藏类型")

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name
    def __str__(self):
        return"{user}_{id}".format(user = self.user.username,id = self.fav_id)

class UserMessage(BaseModel):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name="用户")
    message = models.CharField(max_length=200,verbose_name="消息内容")
    has_read = models.BooleanField(default=False,verbose_name=u"是否已读")

    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.message

class UserPassview(BaseModel):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name="用户")
    company = models.ForeignKey(Company,on_delete=models.CASCADE,verbose_name="浏览记录")
    has_read = models.BooleanField(default=False,verbose_name=u"是否已读")

    class Meta:
        verbose_name = "用户浏览记录"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.company.name