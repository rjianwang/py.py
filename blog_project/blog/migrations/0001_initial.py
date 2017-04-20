# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('avatar', models.ImageField(default=b'avatar/default.png', upload_to=b'avatar/%Y/%m', max_length=200, blank=True, null=True, verbose_name=b'Avatar')),
                ('qq', models.CharField(max_length=20, null=True, verbose_name=b'QQ Number', blank=True)),
                ('mobile', models.CharField(max_length=11, unique=True, null=True, verbose_name=b'Mobile Phone', blank=True)),
                ('url', models.URLField(max_length=100, null=True, verbose_name=b'Web-site', blank=True)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'User',
                'verbose_name_plural': 'User',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name=b'Ads Title')),
                ('description', models.CharField(max_length=200, verbose_name=b'Description')),
                ('image_url', models.ImageField(upload_to=b'ad/%Y/%m', verbose_name=b'Image URL')),
                ('callback_url', models.URLField(null=True, verbose_name=b'Call back URL', blank=True)),
                ('date_publish', models.DateTimeField(auto_now_add=True, verbose_name=b'Publish Date')),
                ('index', models.IntegerField(default=999, verbose_name=b'Sort')),
            ],
            options={
                'ordering': ['index', 'id'],
                'verbose_name': 'Ads',
                'verbose_name_plural': 'Ads',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'Article')),
                ('desc', models.TextField(verbose_name=b'Description')),
                ('content', models.TextField(verbose_name=b'Content')),
                ('click_count', models.IntegerField(default=0, verbose_name=b'Click Count')),
                ('is_recommend', models.BooleanField(default=False, verbose_name=b'Recommend?')),
                ('date_publish', models.DateTimeField(auto_now_add=True, verbose_name=b'Publish Date', db_index=True)),
            ],
            options={
                'ordering': ['-date_publish'],
                'verbose_name': 'Article',
                'verbose_name_plural': 'Article',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'Category')),
                ('index', models.IntegerField(default=999, verbose_name=b'Sort')),
            ],
            options={
                'ordering': ['index', 'id'],
                'verbose_name': 'Category',
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(verbose_name=b'Content')),
                ('username', models.CharField(max_length=30, null=True, verbose_name=b'User', blank=True)),
                ('email', models.EmailField(max_length=50, null=True, verbose_name=b'E-mail', blank=True)),
                ('url', models.URLField(max_length=100, null=True, verbose_name=b'Web-site', blank=True)),
                ('date_publish', models.DateTimeField(auto_now_add=True, verbose_name=b'Publish Date')),
                ('article', models.ForeignKey(verbose_name=b'Article', blank=True, to='blog.Article', null=True)),
                ('pid', models.ForeignKey(verbose_name=b'Parent Comment', blank=True, to='blog.Comment', null=True)),
                ('user', models.ForeignKey(verbose_name=b'User', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comment',
            },
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name=b'Title')),
                ('description', models.CharField(max_length=200, verbose_name=b'Description')),
                ('callback_url', models.URLField(verbose_name=b'URL Address')),
                ('date_publish', models.DateTimeField(auto_now_add=True, verbose_name=b'Publish Date')),
                ('index', models.IntegerField(default=999, verbose_name=b'Sort')),
            ],
            options={
                'ordering': ['index', 'id'],
                'verbose_name': 'Links',
                'verbose_name_plural': 'Links',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'Tag Name')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tag',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(verbose_name=b'Category', blank=True, to='blog.Category', null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag', null=True, verbose_name=b'Tag', blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(verbose_name=b'User', to=settings.AUTH_USER_MODEL),
        ),
    ]
