# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 13:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rasacore', '0008_auto_20171115_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoryActionsResponses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=240)),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='rasacore.StoryActions')),
            ],
        ),
    ]