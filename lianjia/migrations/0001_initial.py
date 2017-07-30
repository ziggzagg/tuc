# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_scraper', '0017_added_order_to_scraped_obj_attr'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoldFlat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=1000)),
                ('address', models.CharField(max_length=100)),
                ('size', models.FloatField(default=-1)),
                ('n_livingroom', models.IntegerField(default=-1)),
                ('n_bedroom', models.IntegerField(default=-1)),
                ('district', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('floor', models.CharField(max_length=100)),
                ('age', models.CharField(default='None', max_length=10)),
                ('sold_date', models.DateField()),
                ('average_price', models.FloatField(default=-1)),
                ('total_price', models.IntegerField(default=-1)),
                ('url', models.URLField(blank=True)),
                ('checker_runtime', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='dynamic_scraper.SchedulerRuntime', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('scraper', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='dynamic_scraper.Scraper', null=True)),
                ('scraper_runtime', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='dynamic_scraper.SchedulerRuntime', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='soldflat',
            name='website',
            field=models.ForeignKey(to='lianjia.Website'),
        ),
    ]
