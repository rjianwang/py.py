# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_publish',
            field=models.DateField(auto_now_add=True, verbose_name=b'Publish Date', db_index=True),
        ),
    ]
