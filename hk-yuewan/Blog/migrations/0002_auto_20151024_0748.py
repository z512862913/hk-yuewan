# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='msg',
            old_name='StratTime',
            new_name='StartTime',
        ),
    ]
