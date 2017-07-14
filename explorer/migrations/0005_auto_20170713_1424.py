# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0004_querylog_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='snapshot',
            field=models.BooleanField(help_text='Include in snapshot task (if enabled)', default=False),
            preserve_default=True,
        ),
    ]
