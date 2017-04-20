# -*- coding: utf-8 -*-

import sys
from django.db import models
from django.contrib.auth.models import AbstractUser

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

# Create your models here.

# 用户模型.
# 第一种：采用的继承方式扩展用户信息（本系统采用）
# 扩展：关联的方式去扩展用户信息
class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default.png', max_length=200, blank=True, null=True, verbose_name='Avatar')
    qq = models.CharField(max_length=20, blank=True, null=True, verbose_name='QQ Number')
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='Mobile Phone')
    url = models.URLField(max_length=100, blank=True, null=True, verbose_name='Web-site')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.username

# tag（标签）
class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='Tag Name')

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

# 分类
class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Category')
    index = models.IntegerField(default=999,verbose_name='Sort')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __unicode__(self):
        return self.name

# 自定义一个文章Model的管理器
# 1、新加一个数据处理的方法
# 2、改变原有的queryset
class ArticleManager(models.Manager):
    def distinct_date(self):
        distinct_date_list = []
        date_list = self.values('date_publish')
        for date in date_list:
            date = date['date_publish'].strftime('%B %Y')
            if date not in distinct_date_list:
                distinct_date_list.append(date)
        return distinct_date_list

# 文章模型
class Article(models.Model):
    title = models.CharField(max_length = 200, verbose_name='Article')
    desc = models.TextField(verbose_name='Description')
    content = models.TextField(verbose_name='Content')
    click_count = models.IntegerField(default=0, verbose_name='Click Count')
    is_recommend = models.BooleanField(default=False, verbose_name='Recommend?')
    date_publish = models.DateField(auto_now_add=True, verbose_name='Publish Date', db_index = True)
    user = models.ForeignKey(User, verbose_name='User')
    category = models.ForeignKey(Category, blank=True, null=True, verbose_name='Category', db_index = True)
    tag = models.ManyToManyField(Tag, verbose_name='Tag', null = True, blank = True)

    objects = ArticleManager()

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']
	
    def __unicode__(self):
        return self.title

# 评论模型
class Comment(models.Model):
    content = models.TextField(verbose_name='Content')
    username = models.CharField(max_length=30, blank=True, null=True, verbose_name='User')
    email = models.EmailField(max_length=50, blank=True, null=True, verbose_name='E-mail')
    url = models.URLField(max_length=100, blank=True, null=True, verbose_name='Web-site')
    date_publish = models.DateField(auto_now_add=True, verbose_name='Publish Date')
    user = models.ForeignKey(User, blank=True, null=True, verbose_name='User')
    article = models.ForeignKey(Article, blank=True, null=True, verbose_name='Article')
    pid = models.ForeignKey('self', blank=True, null=True, verbose_name='Parent Comment')

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return str(self.id)

# 友情链接
class Links(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    description = models.CharField(max_length=200, verbose_name='Description')
    callback_url = models.URLField(verbose_name='URL Address')
    date_publish = models.DateField(auto_now_add=True, verbose_name='Publish Date')
    index = models.IntegerField(default=999, verbose_name='Sort')

    class Meta:
        verbose_name = 'Links'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __unicode__(self):
        return self.title

# 广告
class Ad(models.Model):
    title = models.CharField(max_length=50, verbose_name='Ads Title')
    description = models.CharField(max_length=200,  verbose_name='Description')
    image_url = models.ImageField(upload_to='ad/%Y/%m', verbose_name='Image URL')
    callback_url = models.URLField(null=True, blank=True, verbose_name='Call back URL')
    date_publish = models.DateField(auto_now_add=True, verbose_name='Publish Date')
    index = models.IntegerField(default=999, verbose_name='Sort')

    class Meta:
        verbose_name = u'Ads'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __unicode__(self):
        return self.title
