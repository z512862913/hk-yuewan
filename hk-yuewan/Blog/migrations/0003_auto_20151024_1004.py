# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_auto_20151024_0748'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='msg',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='msg',
            name='people',
            field=models.IntegerField(default=0),
        ),
    ]
