# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-29 09:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0006_auto_20180528_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.TextField(default='default answer', help_text='Copy the text of the correct option and past it here'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='first_option',
            field=models.TextField(default='first_option'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='fourth_option',
            field=models.TextField(default='fourth option'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='second_option',
            field=models.TextField(default='second option'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='third_option',
            field=models.TextField(default='ak'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Quiz'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Course'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]