# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-22 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0055_auto_20160923_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='branch',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='college_year',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='graduation_year',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='programme',
            field=models.CharField(max_length=15),
        ),
    ]
