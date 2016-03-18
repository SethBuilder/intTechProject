# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20160316_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='information',
            field=models.CharField(default=b'', max_length=3000),
            preserve_default=True,
        ),
    ]
