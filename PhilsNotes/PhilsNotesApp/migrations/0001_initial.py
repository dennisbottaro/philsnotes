# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-10 06:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=50)),
                ('job_address', models.CharField(max_length=50)),
                ('job_city', models.CharField(max_length=50)),
                ('job_county', models.CharField(max_length=50)),
                ('builder', models.CharField(max_length=50)),
                ('customer_name', models.CharField(max_length=100)),
                ('home_phone', models.CharField(max_length=20)),
                ('cell_phone', models.CharField(max_length=20)),
                ('cell_phone_2', models.CharField(max_length=20)),
                ('work_phone', models.CharField(max_length=20)),
                ('email_1', models.CharField(max_length=75)),
                ('email_2', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='JobNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_date', models.DateField()),
                ('note_text', models.CharField(max_length=2048)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PhilsNotesApp.Job')),
            ],
        ),
    ]
