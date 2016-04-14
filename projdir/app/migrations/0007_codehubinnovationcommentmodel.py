# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-14 10:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0006_auto_20160413_0452'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodehubInnovationCommentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', django_markdown.models.MarkdownField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('innovation_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.CodehubInnovationPostModel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
