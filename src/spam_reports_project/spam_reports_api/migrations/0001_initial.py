# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-10 10:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PayloadItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=255)),
                ('reportType', models.CharField(max_length=255)),
                ('message', models.CharField(blank=True, max_length=4000)),
                ('reportId', models.CharField(max_length=255)),
                ('referenceResourceId', models.CharField(max_length=255)),
                ('referenceResourceType', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ReferenceItem',
            fields=[
                ('referenceId', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('referenceType', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SpamReportsItem',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('source', models.CharField(max_length=255)),
                ('sourceIdentityId', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('payload', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spam_reports_api.PayloadItem')),
                ('reference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spam_reports_api.ReferenceItem')),
            ],
        ),
    ]