# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_auto_20151024_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msg',
            name='peoplelist',
            field=models.CharField(default=b'PeopleList:', max_length=999),
        ),
    ]
