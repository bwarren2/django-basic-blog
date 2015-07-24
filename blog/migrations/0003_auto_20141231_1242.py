# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import blog.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20141231_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entry',
            name='modified',
            field=blog.fields.AutoDatetimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]
