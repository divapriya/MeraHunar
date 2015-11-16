# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('counselling', '0002_auto_20150831_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='employment',
            field=multiselectfield.db.fields.MultiSelectField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='user_details',
            name='employment_preference',
            field=models.IntegerField(default=1, verbose_name=[1, 2, 3, 4]),
        ),
        migrations.AddField(
            model_name='user_details',
            name='extra_curricullums',
            field=multiselectfield.db.fields.MultiSelectField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='user_details',
            name='extra_curricullums_preference',
            field=models.IntegerField(default=1, verbose_name=[1, 2, 3, 4]),
        ),
        migrations.AddField(
            model_name='user_details',
            name='personalinterest',
            field=multiselectfield.db.fields.MultiSelectField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='user_details',
            name='personalinterest_preference',
            field=models.IntegerField(default=1, verbose_name=[1, 2, 3, 4]),
        ),
        migrations.AddField(
            model_name='user_details',
            name='qualification',
            field=multiselectfield.db.fields.MultiSelectField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='user_details',
            name='qualification_preference',
            field=models.IntegerField(default=1, verbose_name=[1, 2, 3, 4]),
        ),
    ]
