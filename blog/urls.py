# -*- coding: utf-8 -*-
from django.conf.urls import url
from views import ArticleListView, ArchiveListView

urlpatterns = [
    url(r'^(?P<year_month>\d{4}-\d{2})$', ArchiveListView.as_view(template_name="blog/index.html"),
        name='month-archive-view'),

    url(r'^$', ArticleListView.as_view(template_name="blog/index.html"),
        name='article-list-view'),
]
