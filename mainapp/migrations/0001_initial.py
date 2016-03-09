<<<<<<< HEAD
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', unique=True, max_length=128)),
                ('country', models.CharField(default=b'Scotland', max_length=128)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hobby', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=128)),
                ('email', models.EmailField(unique=True, max_length=128)),
                ('profilepic', models.ImageField(null=True, upload_to=b'')),
                ('firstname', models.CharField(max_length=128, null=True)),
                ('secondname', models.CharField(max_length=128, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('city', models.ForeignKey(to='mainapp.City')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=500)),
                ('for_username', models.CharField(max_length=128)),
                ('rating', models.IntegerField(default=5)),
                ('user', models.ForeignKey(to='mainapp.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='language',
            name='users',
            field=models.ManyToManyField(to='mainapp.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hobby',
            name='users',
            field=models.ManyToManyField(to='mainapp.User'),
            preserve_default=True,
        ),
    ]
||||||| merged common ancestors
=======
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', unique=True, max_length=128)),
                ('country', models.CharField(default=b'Scotland', max_length=128)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hobby', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=128)),
                ('email', models.EmailField(unique=True, max_length=128)),
                ('profilepic', models.ImageField(null=True, upload_to=b'')),
                ('firstname', models.CharField(max_length=128, null=True)),
                ('secondname', models.CharField(max_length=128, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('city', models.ForeignKey(to='mainapp.City')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('user', models.OneToOneField(to='mainapp.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=500)),
                ('for_username', models.CharField(max_length=128)),
                ('rating', models.IntegerField(default=5)),
                ('user', models.ForeignKey(to='mainapp.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='language',
            name='users',
            field=models.ManyToManyField(to='mainapp.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hobby',
            name='users',
            field=models.ManyToManyField(to='mainapp.User'),
            preserve_default=True,
        ),
    ]
>>>>>>> 3f7ac8e858e0485cf415ce12b956d39765cad02e
