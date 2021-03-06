# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-02 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0004_auto_20160708_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='SundayBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.CharField(choices=[('13:00', '13:00'), ('13:15', '13:15'), ('13:30', '13:30'), ('13:45', '13:45'), ('14:00', '14:00'), ('15:30', '15:30'), ('15:45', '15:45'), ('16:00', '16:00'), ('16:15', '16:15'), ('16:30', '16:30')], max_length=5)),
                ('pax', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(default='', max_length=20)),
                ('comments', models.TextField(blank=True, null=True)),
                ('phone', models.PositiveIntegerField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('capacity', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='booking',
            name='table',
        ),
        migrations.AddField(
            model_name='booking',
            name='phone',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='pax',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.CharField(choices=[('18:00', '18:00'), ('18:15', '18:15'), ('18:30', '18:30'), ('18:45', '18:45'), ('19:00', '19:00'), ('19:15', '19:15'), ('19:30', '19:30'), ('19:45', '19:45'), ('20:00', '20:00'), ('20:15', '20:15'), ('20:30', '20:30'), ('20:45', '20:45'), ('21:00', '21:00'), ('21:15', '21:15'), ('21:30', '21:30'), ('21:45', '21:45'), ('22:00', '22:00')], max_length=5),
        ),
        migrations.AddField(
            model_name='sundaybooking',
            name='tables',
            field=models.ManyToManyField(to='calendario.Table'),
        ),
        migrations.AddField(
            model_name='booking',
            name='tables',
            field=models.ManyToManyField(to='calendario.Table'),
        ),
    ]
