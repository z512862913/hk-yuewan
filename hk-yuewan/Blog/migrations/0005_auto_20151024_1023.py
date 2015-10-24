# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_msg_peoplelist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msg',
            name='peoplelist',
            field=models.CharField(default=b'', max_length=999),
        ),
    ]
