# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-05 06:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carousel_pic', models.ImageField(default='mainapp/image/no_img.jpg', upload_to='mainapp/image/')),
                ('carousel_header', models.CharField(default='', max_length=100)),
                ('carousel_text', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
