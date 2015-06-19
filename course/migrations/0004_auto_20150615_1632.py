# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20150613_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseZan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'date publish')),
                ('course', models.ForeignKey(to='course.Course')),
                ('student', models.ForeignKey(to='course.Student')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewZan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'date publish')),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 15, 8, 32, 50, 462000, tzinfo=utc), verbose_name=b'date publish', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reviewzan',
            name='review',
            field=models.ForeignKey(to='course.Review'),
        ),
        migrations.AddField(
            model_name='reviewzan',
            name='student',
            field=models.ForeignKey(to='course.Student'),
        ),
    ]
