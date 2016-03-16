# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20160316_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='average_rating',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='ratings_count',
        ),
    ]
