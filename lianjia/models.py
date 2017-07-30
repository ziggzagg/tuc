# -*- coding: utf-8 -*-

from django.db import models
from dynamic_scraper.models import Scraper, SchedulerRuntime
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from scrapy_djangoitem import DjangoItem
# Create your models here.


def decode(info):
    return info.decode('utf-8')


class Website(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    scraper = models.ForeignKey(Scraper, blank=True, null=True, on_delete=models.SET_NULL)
    scraper_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class SoldFlat(models.Model):
    title = models.CharField(max_length=1000)
    address = models.CharField(max_length=100)
    size = models.FloatField(default=-1)
    n_livingroom = models.IntegerField(default=-1)
    n_bedroom = models.IntegerField(default=-1)
    district = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
#    floor = models.CharField(max_length=100)
    age = models.CharField(max_length=10, default=u'None')

    sold_date = models.DateField()
    average_price = models.FloatField(default=-1)
    total_price = models.IntegerField(default=-1)

    website = models.ForeignKey(Website)
    url = models.URLField(blank=True)
    checker_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.address


class SoldFlatItem(DjangoItem):
    django_model = SoldFlat


@receiver(pre_delete)
def pre_delete_handler(sender, instance, using, **kwargs):
    if isinstance(instance, Website):
        if instance.scraper_runtime:
            instance.scraper_runtime.delete()

    if isinstance(instance, SoldFlat):
        if instance.checker_runtime:
            instance.checker_runtime.delete()

pre_delete.connect(pre_delete_handler)