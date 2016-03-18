# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_city_information'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='image',
            field=models.ImageField(default=datetime.date(2016, 3, 18), upload_to=b'city_images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profilepic',
            field=models.ImageField(upload_to=b'static/images/Profile Pictures', blank=True),
        ),
    ]
