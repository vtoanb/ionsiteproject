# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-05 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20160405_0705'),
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_pic', models.ImageField(default='mainapp/image/no_img.jpg', upload_to='mainapp/static/mainapp/image')),
                ('event_name', models.CharField(default='', max_length=100)),
                ('event_text', models.CharField(default='', max_length=500)),
            ],
        ),
    ]