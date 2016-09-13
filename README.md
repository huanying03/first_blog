# first_blog
linux + python + Django -> webSite "first_blog"

# 本代码来源：

学习imooc上的“django初体验”视频课程，在linux下实际练习产生的可用代码。

# 学习笔记：

## 1 Django简介

Django - Python 的Web框架

### 优点：

- 快速开发：python开发，数据库ORM系统

- 大量内置应用：后台管理系统admin, 用户认证系统auth， 会话系统sessions

- 安全性高：表单验证，SQL注入，跨站点攻击

- 易扩展

### 知识基础：

- Python基础

- SQL

- HTTP协议 

- HTML&CSS - 前端网页知识

- 正则表达式 - 文本处理工具

## 2 django环境搭建

install python2.7

install ipython  

install python-pip  

### install django

[~]$ git clone https://github.com/django/django.git

[~]$ cd django

[~/django]$ python setup.py install

### 创建第一个项目：

[~]$ django-admin startproject mysite

[~]$ cd mysite

### 启动webServer

[~/mysite]$ python manage.py runserver

默认地址：端口为 127.0.0.1:8000

可指定地址：端口

[~/mysite]$ python manage.py runserver 0.0.0.0:8080

### 工程目录详解
manage.py 管理项目：包括数据库建立、服务器运行、测试…… 最常用的有runserver, make migrations, migrate, shell 
- [~/mysite]$ python manage.py create superuser 创建系统员
- [~/mysite]$ python manage.py makemigrations 每次新建模块后的更新指令
- [~/mysite]$ python manage.py migrate 同上
- [~/mysite]$ python manage.py syncdb 数据库同步

~/mysite/mysite 目录

- setttings.py 配置文件： 应用、中间件、数据库、静态目录各类配置

- urls.py URL映射配置文件：决定一个url访问被哪个程序（函数）响应

- wsgi.py Python应用程序或框架和web服务器(Aparch等)之间接口

### 创建应用
- 创建应用blog

[~/mysite]$ python manage.py startapp blog

- 添加blog应用

~/mysite/mysite/settings.py找到“INSTALLED_APPS”项，新增一行

'blog',

### 应用目录详解
#### view.py 响应用户请求返回html页面

- ~/mysite/blog/views.py

新增函数：
def hello(request):
    return HttpResponse('<html>Hello World</html>')
    
- ~/mysite/mysite/urls.py

urlpatterns=[

url(r'helloworld','blog.views.hello')
]

访问地址：//127.0.0.1:8000/helloworld

#### ~/mysite/blog/models.py 定义数据库中的表
#### ~/mysite/blog/admin.py 管理用
#### ~/mysite/blog/test.py 测试用
#### ~/mysite/blog/migrations/ 与数据库相关

## 3 django初体验

### 一次web访问的实质

- 客户发送http请求到web服务器

- web服务器返回html页面给客户

### Django中的重要概念

- URL配置：建立URL与响应函数之间的关系

- 视图views:响应客户http请求，进行逻辑处理，返回给用户html页面

- 模型Models:描述服务器存储的数据（数据库的表）

- 模板templates:用来生产html页面，返回给用户的html，是由数据（模型）和模板渲染出来的

#### ~/mysite/mysite/urls.py 配置URL和响应函数之间的关系
url(r'^$','blog.views.showBlogList'),

url(r'^blog/(\d+)$','blog.views.showBlog'),

#### ~/mysite/blog/views.py 响应客户http请求，返回给用户html页面
from django.shortcut import render

from models import Blog 
...
#### ~/mysite/blog/models.py 数据记录定义（数据库中的表）

#### ~/mysite/blog/templates/blog.html  html页面

#### 
