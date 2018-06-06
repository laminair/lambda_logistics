# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-17 01:46
from __future__ import unicode_literals

import corelogistics.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('city', models.CharField(max_length=70, unique=True)),
                ('address', models.CharField(max_length=70)),
                ('type', models.CharField(choices=[('Headquarter', 'Headquarter'), ('Regional Hub', 'Regional Hub'), ('Satellite Office', 'Satellite Office')], max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_n', models.CharField(default=corelogistics.models.gen_tracking_no, max_length=8, unique=True)),
                ('confirmed', models.BooleanField(default=False)),
                ('r_id_req', models.BooleanField(default=False)),
                ('p_height', models.PositiveIntegerField()),
                ('p_width', models.PositiveIntegerField()),
                ('p_depth', models.PositiveIntegerField()),
                ('weight', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('Created', 'CREATED'), ('Fetched', 'FETCHED'), ('In Hub Inbound', 'IN HUB INBOUND'), ('In Hub Outbound', 'IN HUB OUTBOUND'), ('In Transit', 'IN TRANSIT'), ('Delivered', 'DELIVERED'), ('Delivery Failed', 'DELIVERY FAILED')], default='Created', max_length=25)),
                ('failed', models.IntegerField(blank=True, default=0)),
                ('distance', models.IntegerField()),
                ('sender_first_name', models.CharField(max_length=70)),
                ('sender_surname', models.CharField(max_length=70)),
                ('sender_address', models.CharField(max_length=100)),
                ('sender_zip', models.IntegerField()),
                ('recipient_first_name', models.CharField(max_length=70)),
                ('recipient_surname', models.CharField(max_length=70)),
                ('recipient_address', models.CharField(max_length=100)),
                ('recipient_zip', models.IntegerField(null=True)),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('date_fetched', models.DateField(blank=True, null=True)),
                ('date_inhub', models.DateField(blank=True, null=True)),
                ('date_intransit', models.DateField(blank=True, null=True)),
                ('date_delivered', models.DateField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('current_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='corelogistics.Office')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('recipient_city', models.ForeignKey(default='Cape Town Central - Airport', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='corelogistics.Office', to_field='city')),
                ('sender_city', models.ForeignKey(default='Cape Town Central - Airport', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='corelogistics.Office', to_field='city')),
            ],
        ),
    ]