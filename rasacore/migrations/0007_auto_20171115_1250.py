# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 12:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rasacore', '0006_auto_20171115_0711'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoryActions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='story_actions', to='rasacore.Actions')),
            ],
        ),
        migrations.RemoveField(
            model_name='stories',
            name='actions',
        ),
        migrations.AddField(
            model_name='storyactions',
            name='story',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='rasacore.Stories'),
        ),
    ]