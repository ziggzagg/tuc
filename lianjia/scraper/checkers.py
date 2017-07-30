from __future__ import unicode_literals
from dynamic_scraper.spiders.django_checker import DjangoChecker
from lianjia.models import SoldFlat


class SoldFlatChecker(DjangoChecker):
    
    name = 'soldflat_checker'
    
    def __init__(self, *args, **kwargs):
        self._set_ref_object(SoldFlat, **kwargs)
        self.scraper = self.ref_object.website.scraper
        self.scheduler_runtime = self.ref_object.checker_runtime
        super(SoldFlatChecker, self).__init__(self, *args, **kwargs)