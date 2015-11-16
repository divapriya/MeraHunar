# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counselling', '0003_auto_20150902_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_individual',
            name='by',
            field=models.ForeignKey(to='users.Users'),
        ),
        migrations.AlterField(
            model_name='comment_organization',
            name='by',
            field=models.ForeignKey(to='users.Users'),
        ),
        migrations.AlterField(
            model_name='individual_details',
            name='details',
            field=models.ForeignKey(to='users.Freelancers'),
        ),
        migrations.AlterField(
            model_name='organization_details',
            name='details',
            field=models.ForeignKey(to='users.Organizers'),
        ),
        migrations.AlterField(
            model_name='ranking_individual',
            name='by',
            field=models.ForeignKey(to='users.Users'),
        ),
        migrations.AlterField(
            model_name='ranking_organization',
            name='by',
            field=models.ForeignKey(to='users.Users'),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='details',
            field=models.ForeignKey(to='users.Users'),
        ),
    ]
