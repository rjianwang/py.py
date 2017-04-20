from django.conf.urls import url
from blog.views import *
 
urlpatterns = [
	url(r'^$', index, name = 'index'),	
	url(r'^archive/$', archive, name = "archive"),
	url(r'^article/$', article, name = 'article'),
	url(r'^category/$', category, name = 'category'),
	url(r'^comment/$', comment_post, name = 'comment_post'),
	url(r'^contact/$', contact_post, name = 'contact_post'),
	url(r'^search/$', search_get, name = 'search_get'),
	url(r'^index.html$', index, name = 'index'),
	url(r'^post.html$', post, name = 'post'),
	url(r'^post/$', post, name = 'post'),
	url(r'^about.html$', about, name = 'about'),
	url(r'^contact.html$', contact, name = 'contact'),
]
