# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_user_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hobby',
            name='user',
        ),
        migrations.RemoveField(
            model_name='language',
            name='user',
        ),
        migrations.AddField(
            model_name='hobby',
            name='users',
            field=models.ManyToManyField(to='mainapp.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='language',
            name='users',
            field=models.ManyToManyField(to='mainapp.User'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(default=b'', unique=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='city',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
