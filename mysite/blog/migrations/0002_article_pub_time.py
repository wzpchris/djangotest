# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-09 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
