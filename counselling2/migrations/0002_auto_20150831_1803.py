# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counselling', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='individual_details',
            name='slug',
            field=models.SlugField(unique=True, null=True),
        ),
        migrations.AddField(
            model_name='organization_details',
            name='slug',
            field=models.SlugField(unique=True, null=True),
        ),
        migrations.AddField(
            model_name='user_details',
            name='slug',
            field=models.SlugField(unique=True, null=True),
        ),
    ]
