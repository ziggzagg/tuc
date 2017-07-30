# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from dynamic_scraper.spiders.django_spider import DjangoSpider
from lianjia.models import SoldFlat, Website, SoldFlatItem


class SoldFlatSpider(DjangoSpider):
    
    name = 'soldflat_spider'

    def __init__(self, *args, **kwargs):
        self._set_ref_object(Website, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = self.ref_object.url
        self.scheduler_runtime = self.ref_object.scraper_runtime
        self.scraped_obj_class = SoldFlat
        self.scraped_obj_item_class = SoldFlatItem
        super(SoldFlatSpider, self).__init__(self, *args, **kwargs)