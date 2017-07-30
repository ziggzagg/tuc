# -*- coding: utf-8 -*-
from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', SoldFlatCount.as_view()),
    url(r'^(?P<key>[\w-]+)/$', fetch_ajax, name='fetch_ajax'),
]
