from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    '''
    用户
    '''
    name = models.CharField(max_length=30,null=True,blank=True,verbose_name='姓名')
    birthday = models.DateField(null=True,blank=True,verbose_name='出生年月')
    gender = models.CharField(max_length=6,choices=(("male","男"),('female','女')),default="female",verbose_name="性别")
    mobile = models.CharField(null=True,blank=True,max_length=11,verbose_name='电话')
    email = models.EmailField(max_length=100,null=True,blank=True,verbose_name='邮箱')
    # Django models里面blank和null的用法区别    https://blog.csdn.net/rampage_chopper/article/details/80268341
    class Meta:
        verbose_name = '用户'                 #定义实体类在admin中显示的名字（单数）
        verbose_name_plural = verbose_name          #定义实体类在admin中显示的名字（复数）

    def __str__(self):
        return self.username

class VerifyCode(models.Model):
    """
    短信验证
    """
    code = models.CharField(max_length=10,verbose_name='验证码')
    mobile = models.CharField(max_length=11,verbose_name='电话')
    add_time = models.DateTimeField(default=datetime.now(),verbose_name="添加时间")

    class Meta:
        verbose_name = '短信验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code

















