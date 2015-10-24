# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Msg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.GenericIPAddressField()),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=9999)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=20)),
                ('StratTime', models.DateTimeField()),
                ('EndTime', models.DateTimeField()),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
