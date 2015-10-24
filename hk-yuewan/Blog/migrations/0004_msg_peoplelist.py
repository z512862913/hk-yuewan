# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_auto_20151024_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='msg',
            name='peoplelist',
            field=models.CharField(default=datetime.datetime(2015, 10, 24, 10, 20, 7, 805885, tzinfo=utc), max_length=999),
            preserve_default=False,
        ),
    ]
