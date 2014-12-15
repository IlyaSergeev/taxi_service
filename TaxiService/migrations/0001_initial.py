# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brand', models.CharField(max_length=64)),
                ('model', models.CharField(max_length=64)),
                ('color', models.CharField(max_length=64)),
                ('reg_number', models.CharField(max_length=16)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
                ('car', models.ForeignKey(to='TaxiService.Car', unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('driverEmail', models.EmailField(max_length=75)),
                ('fromAddress', models.CharField(max_length=256)),
                ('toAddress', models.CharField(max_length=256)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(to='TaxiService.Car')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
