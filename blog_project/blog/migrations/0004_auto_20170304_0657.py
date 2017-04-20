# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170304_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='date_publish',
            field=models.DateField(auto_now_add=True, verbose_name=b'Publish Date'),
        ),
        migrations.AlterField(
            model_name='links',
            name='date_publish',
            field=models.DateField(auto_now_add=True, verbose_name=b'Publish Date'),
        ),
    ]
