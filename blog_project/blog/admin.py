# -*- coding: utf-8 -*-

from django.contrib import admin
from models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
	
	list_display = ('username', 'email', 'is_active', 'is_superuser', 'date_joined', 'mobile')
	list_display_links = ('username', )
	search_fields = ('username', 'email', 'mobile')

class ArticleAdmin(admin.ModelAdmin):

	list_display = ('title', 'user', 'category', 'date_publish', 'is_recommend')
	list_filter = ('category', 'date_publish', )

	fieldsets = (
		(None, {
			'fields': ('title', 'content', 'desc', 'user', 'category', 'is_recommend', )
		}),
		('Advanced Options', {
			'classes': ('collapse',),
			'fields': ('tag', 'click_count', )
		}),
	)
	search_fields = ('date_publish',)

	class Media:
		js = (
			'/static/js/kindeditor-4.1.10/kindeditor-min.js',
			'/static/js/kindeditor-4.1.10/lang/zh_CN.js',
			'/static/js/kindeditor-4.1.10/config.js',
		)

class CommentAdmin(admin.ModelAdmin):
	
	list_display = ('content', 'article', 'date_publish', 'username', 'email')
	search_fields = ('username', 'content', 'article', 'email', 'date_publish')
	list_filter = ('date_publish', )

class LinksAdmin(admin.ModelAdmin):
	
	list_display = ('title', 'callback_url', 'description', 'date_publish')
	search_fields = ('title', 'callback_url', 'description', 'date_publish')

class AdAdmin(admin.ModelAdmin):
	
	list_display = ('title', 'description', 'callback_url', 'image_url', 'date_publish')
	search_fields = ('title', 'description', 'callback_url', 'date_publish')


admin.site.register(User, UserAdmin)
admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Links, LinksAdmin)
admin.site.register(Ad, AdAdmin)
