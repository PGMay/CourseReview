# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_course_course_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursezan',
            name='like',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reviewzan',
            name='like',
            field=models.BooleanField(default=False),
        ),
    ]
