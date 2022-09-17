# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-25 15:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classroom', '0003_auto_20180523_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teaching_assistants',
            field=models.ManyToManyField(related_name='teaching_assistant', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(related_name='students', to=settings.AUTH_USER_MODEL),
        ),
    ]
