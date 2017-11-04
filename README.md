<!--
@Author: 魏巍
@Date:   2017-11-02T10:49:17+08:00
@Email:  524314430@qq.com
@Last modified by:   魏巍
@Last modified time: 2017-11-02T14:42:25+08:00
-->



# Django项目练习

> 根据项目来学习Django[链接](https://docs.djangoproject.com/en/1.11/intro/tutorial01/)学习网址

* 创建项目

  1. `django-admin startproject mysite`   #创建工程
  2. `python manage.py startapp polls`    #创建项目
  3. `python manage.py runserver`         #运行项目


* 创建数据模型

  1. `polls/models.py` 创建对象
  2. 在 `mysite/settings.py`中`INSTALLED_APPS`添加自己的项目名
     ```python
     INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'polls',    #添加项目
    )
     ```
 3. `python manage.py makemigrations` 现在通知Django，已经对模型做了一些更改（在这个例子中，你创建了一个新的模型）并且会将这些更改记录为迁移文件
 4. `python manage.py migrate` 数据库中创建模型所对应的表
 
