# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-10 23:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='post_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
