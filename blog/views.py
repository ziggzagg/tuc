# -*- coding: utf-8 -*-
from datetime import datetime

import pytz
from dateutil import relativedelta
from django.conf import settings
from django.views.generic import ListView

from models import Article


class ArticleListView(ListView):
    model = Article
    context_object_name = "article_list"

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context["pub_month_list"] = __get_pub_month_list__()
        return context


class ArchiveListView(ListView):
    model = Article
    context_object_name = "article_list"

    def get_queryset(self):
        year_month = self.kwargs['year_month']
        target = datetime.strptime(year_month, "%Y-%m").replace(tzinfo=pytz.timezone(settings.TIME_ZONE))
        delta = relativedelta.relativedelta(months=1)
        return Article.objects.filter(publish_date__gte=target,
                                      publish_date__lt=target + delta)

    def get_context_data(self, **kwargs):
        kwargs["pub_month_list"] = __get_pub_month_list__
        return super(ArchiveListView, self).get_context_data(**kwargs)


def __get_pub_month_list__():
    query_set = Article.objects.values('publish_date')
    year_month_set = set()
    for i in query_set:
        year_month_set.add(i['publish_date'].strftime('%Y-%m'))
    ret = list(year_month_set)
    ret.sort(reverse=True)
    return ret