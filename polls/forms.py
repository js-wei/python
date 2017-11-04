# @Author: 魏巍
# @Date:   2017-11-04T13:05:42+08:00
# @Email:  524314430@qq.com
# @Last modified by:   魏巍
# @Last modified time: 2017-11-04T15:59:23+08:00

from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class ArticleForm(forms.Form):
    title = forms.CharField(label='标题', max_length=100)
    author = forms.CharField(label='作者', max_length=100)
    keywords = forms.CharField(label='关键词', max_length=100)
    description = forms.CharField(label='介绍', max_length=100)
    image = forms.FileField(label='图片')
    content = forms.CharField(label='内容', max_length=100)
