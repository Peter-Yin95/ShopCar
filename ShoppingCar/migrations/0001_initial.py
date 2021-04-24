# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyCars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductID', models.CharField(max_length=18)),
                ('ProductName', models.CharField(max_length=30)),
                ('ProductPrice', models.PositiveIntegerField()),
            ],
        ),
    ]
