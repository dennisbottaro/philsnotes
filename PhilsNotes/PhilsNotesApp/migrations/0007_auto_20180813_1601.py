# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-08-13 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PhilsNotesApp', '0006_auto_20180813_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobnote',
            name='note_date',
            field=models.DateField(db_index=True),
        ),
    ]
