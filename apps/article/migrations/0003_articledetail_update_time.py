# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-23 07:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20180223_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='articledetail',
            name='update_time',
            field=models.DateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间'),
        ),
    ]