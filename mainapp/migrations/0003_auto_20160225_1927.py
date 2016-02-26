# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20160225_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobby',
            name='hobby',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='language',
            name='language',
            field=models.CharField(max_length=128),
        ),
    ]
