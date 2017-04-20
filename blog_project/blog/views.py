# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.conf import settings
from django.db.models import Q
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from models import *
from forms import *
from mail import *
import time, datetime
import logging

logger = logging.getLogger('blog.views')

# Create your views here.

def global_setting(request):
	# 站点基本信息
	SITE_NAME = settings.SITE_NAME
	SITE_DESC = settings.SITE_DESC
	ADMIN     = settings.ADMIN
	ADDRESS   = settings.ADDRESS
	PHONE     = settings.PHONE
	EMAIL     = settings.EMAIL

	try:
		# 获取文章
		recommend_list  = Article.objects.filter(is_recommend = 1)[:5]
		# 文章分类数据
		category_list = Category.objects.all()		
		# 文章归档
		# 获取文章中有的 月份-年份
		archive_list = Article.objects.distinct_date()[:5]
		# 定义搜索表单
		search_form = SearchForm({"search": ""})
	except Exception as e:
		logger.error(e)
	return locals()

def index(request):
	try:
		# 获取最新文章数据并分页显示
		article_list = Article.objects.all()
		article_list = getPage(request, article_list)
	except Exception as e:
		logger.error(e)
	
	return render(request, 'index.html', locals())

def archive(request):
	try:
		# 文章归档（显示归档文档）
		year = request.GET.get('year', None)
		month = request.GET.get('month', None)
		date = datetime.datetime.strptime(year + '-' + month, '%Y-%B').strftime('%Y-%m')
		article_list = Article.objects.filter(date_publish__icontains = date)
		article_list = getPage(request, article_list)
	except Exception as e:
		logger.error(e)
		return render(request, '404.html', {'reason': 'The request page does not exist.'})
	return render(request, 'archive.html', locals())

def category(request):
	try:
		cid = request.GET.get('cid', None)
		try:
			article_list = Article.objects.filter(category_id = cid)
			article_list = getPage(request, article_list)
		except Category.DoesNotExist:
			return render(request, '404.html', {'reason': 'The request page does not exist.'})
	except Exception as e:
		logger.error(e)
	return render(request, 'category.html', locals())

def getPage(request, article_list):
	paginator = Paginator(article_list, 5)
	try:
		page = int(request.GET.get('page', 1))
		article_list = paginator.page(page)
	except (EmptyPage, InvalidPage, PageNotAnInteger):
		article_list = paginator.page(1)
	return article_list

def article(request):
	try:
		id = request.GET.get('id', None)
		try:
			# 获取文章信息
			article = Article.objects.get(pk = id)
		except Article.DoesNotExist:
			return render(request, '404.html', {'reason': 'The request article does not exist.'})

		# 获取评论信息
		comments = Comment.objects.filter(article=article).order_by('id')
		comment_list = []
		for comment in comments:
			for item in comment_list:
				if not hasattr(item, 'children_comment'):
					setattr(item, 'children_comment', [])
				if comment.pid == item:
					item.children_comment.append(comment)
					break
			if comment.pid is None:
				comment_list.append(comment)
		# 评论表单
		comment_form = CommentForm({'author': "", "email": "", "article": id})

	except Exception as e:
		logger.error(e)

	return render(request, 'article.html', locals())

# 提交评论
def comment_post(request):
	try:
		comment_form = CommentForm(request.POST)
		if comment_form.is_valid():
			#获取表单信息
			comment = Comment.objects.create(
								 username = comment_form.cleaned_data["author"],
                                 email = comment_form.cleaned_data["email"],
                                 content = comment_form.cleaned_data["comment"],
                                 article_id = comment_form.cleaned_data["article"],
                                 user = request.user)
			comment.save()
		else:
			return render(request, '404.html', {'reason': comment_form.errors})
	except Exception as e:
		logger.error(e)
	return redirect(request.META['HTTP_REFERER'])

def contact_post(request):
	try:
		contact_form = ContactForm(request.POST)
		if contact_form.is_valid():
			# 获取表单信息
			username = contact_form.cleaned_data["author"]
			email = contact_form.cleaned_data["email"]
			message  = contact_form.cleaned_data["message"]
			sendmail(settings.EMAIL, settings.EMAIL, 'username', message)
	except Exception as e:
		logger.error(e)
	return redirect(request.META['HTTP_REFERER'])

def search_get(request):
	search = request.GET.get('search', None)
	try:
		# 获取文章信息
		article_list = Article.objects.filter(Q(title__icontains = search) 
			| Q(content__icontains = search)
			| Q(date_publish__icontains = search)
			| Q(category__name__icontains = search))
		article_list = getPage(request, article_list)
	except Article.DoesNotExist:
		return render(request, '404.html', {'reason': 'The request article does not exist.'})

	return render(request, "post.html", locals())

def post(request):
	try:
		cid = request.GET.get('cid', None)
		try:
			if cid is not None:
				article_list = Article.objects.filter(category_id = cid)
			else:
				article_list = Article.objects.all()
	
			# 分页
			article_list = getPage(request, article_list)
		except Category.DoesNotExist:
			return render(request, '404.html', {'reason': 'The request page does not exist.'})
	except Exception as e:
		logger.error(e)
	
	return render(request, 'post.html', locals())

def about(request):
	return render(request, 'about.html', locals())

def contact(request):
	contact_form = ContactForm({"author": "", "email": ""})
	return render(request, 'contact.html', locals())
