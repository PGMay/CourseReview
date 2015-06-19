# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_remove_student_sid'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_type',
            field=models.IntegerField(default=0, choices=[(0, '\u516c\u5fc5'), (1, '\u516c\u9009'), (2, '\u4e13\u5fc5'), (3, '\u4e13\u9009')]),
            preserve_default=False,
        ),
    ]
