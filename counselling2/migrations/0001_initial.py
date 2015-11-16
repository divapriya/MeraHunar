# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150831_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment_Individual',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment_Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Individual_Details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'anonymous user', max_length=200)),
                ('details', models.ForeignKey(to='users.Drinker')),
            ],
        ),
        migrations.CreateModel(
            name='Organization_Details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'anonymous user', max_length=200)),
                ('details', models.ForeignKey(to='users.Drinker')),
            ],
        ),
        migrations.CreateModel(
            name='Ranking_Individual',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ranking', models.FloatField(null=True, blank=True)),
                ('attribute', models.ForeignKey(to='counselling.Individual_Details')),
                ('by', models.ForeignKey(to='users.Drinker')),
            ],
        ),
        migrations.CreateModel(
            name='Ranking_Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ranking', models.FloatField(null=True, blank=True)),
                ('attribute', models.ForeignKey(to='counselling.Organization_Details')),
                ('by', models.ForeignKey(to='users.Drinker')),
            ],
        ),
        migrations.CreateModel(
            name='User_Details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'anonymous user', max_length=200)),
                ('details', models.ForeignKey(to='users.Drinker')),
            ],
        ),
        migrations.AddField(
            model_name='comment_organization',
            name='attribute',
            field=models.ForeignKey(to='counselling.Organization_Details'),
        ),
        migrations.AddField(
            model_name='comment_organization',
            name='by',
            field=models.ForeignKey(to='users.Drinker'),
        ),
        migrations.AddField(
            model_name='comment_individual',
            name='attribute',
            field=models.ForeignKey(to='counselling.Individual_Details'),
        ),
        migrations.AddField(
            model_name='comment_individual',
            name='by',
            field=models.ForeignKey(to='users.Drinker'),
        ),
    ]
