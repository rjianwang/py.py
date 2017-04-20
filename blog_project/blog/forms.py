# -*- coding:utf-8 -*-
from django import forms
from django.conf import settings
from django.db.models import Q
import re

# 联系表单
class ContactForm(forms.Form):
	author = forms.CharField(widget = forms.TextInput(attrs = {"id": "author", "class": "author", "required": "required"}), max_length = 50, error_messages = {"required":"User name cannot be blank",})
	email = forms.EmailField(widget = forms.TextInput(attrs = {"id": "email",  "class": "email", "required": "required"}), max_length = 50, error_messages = {"required": "Email cannot be blank",})
	message = forms.CharField(widget = forms.Textarea(attrs = {"id": "message", "class": "message", "required": "required"}), error_messages={"required": "Message cannot be blank",})


# 评论表单
class CommentForm(forms.Form):
	author = forms.CharField(widget = forms.TextInput(attrs = {"id": "author", "class": "author", "required": "required"}), max_length = 50, error_messages = {"required":"User name cannot be blank",})
	email = forms.EmailField(widget = forms.TextInput(attrs = {"id": "email",  "class": "email", "required": "required"}), max_length = 50, error_messages = {"required": "Email cannot be blank",})
	comment = forms.CharField(widget = forms.Textarea(attrs = {"id": "comment", "class": "comment", "required": "required"}), error_messages={"required": "Comment cannot be blank",})
	article = forms.CharField(widget = forms.HiddenInput())

# 查询表单
class SearchForm(forms.Form):
	search = forms.CharField(widget = forms.TextInput(attrs = {"type": "search", "placeholder": "Search", "required": "required"}), max_length = 100, error_messages = {"required": "Search content cannot be blank"})
