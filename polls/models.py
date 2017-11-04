# @Author: 魏巍
# @Date:   2017-11-02T10:48:18+08:00
# @Email:  524314430@qq.com
# @Last modified by:   魏巍
# @Last modified time: 2017-11-04T16:07:30+08:00


import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    title = models.CharField(u'标题', max_length=256)
    author = models.CharField(u'作者', max_length=256,default='')
    keywords = models.CharField(u'关键词', max_length=256,default='')
    description = models.CharField(u'介绍', max_length=256,default='')
    image = models.CharField(u'介绍', max_length=256,default='')
    content = models.TextField(u'内容')
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable = True)
    update_time = models.DateTimeField(u'更新时间',auto_now=True, null=True)
    hits = models.IntegerField(u'阅读量',default=0)
    status = models.BooleanField(u'状态',default=True)
    def __str__(self):
        return self.title
