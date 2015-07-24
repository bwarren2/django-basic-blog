# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20141231_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='publicity',
            field=models.IntegerField(default=2, choices=[(0, b'Public'), (1, b'Login'), (2, b'Private')]),
            preserve_default=True,
        ),
    ]
