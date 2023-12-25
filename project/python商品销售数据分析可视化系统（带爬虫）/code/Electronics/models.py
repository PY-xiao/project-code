from django.db import models
from django.contrib.auth.models import User,AbstractUser

# Create your models here.

class Users(AbstractUser):
    set_choices = (
        ('男','男'),
        ('女','女')
    )
    age = models.CharField(verbose_name='年龄',max_length=16,default='18')
    set = models.CharField(verbose_name='性别',max_length=12,default='男',choices=set_choices)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = u"用户表"
        verbose_name_plural = u"用户表"

class XinXi(models.Model):
    name = models.CharField(verbose_name='标题',default='',max_length=32)
    url = models.CharField(verbose_name='链接',default='',max_length=32)
    price = models.FloatField(verbose_name='价格',default=0.0)
    shopname = models.CharField(verbose_name='店铺名',default='',max_length=32)
    pinpai = models.CharField(verbose_name='品牌',default='',max_length=32)
    xinghao = models.CharField(verbose_name='型号', default='', max_length=32)
    haoping = models.FloatField(verbose_name='好评率',default=0.0)
    chaping = models.FloatField(verbose_name='差评数', default=0.0)
    count = models.FloatField(verbose_name='销售数',default=0.0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"信息表"
        verbose_name_plural = verbose_name





