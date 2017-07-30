# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings


def decode(info):
    return info.decode('utf-8')


class Article(models.Model):
    title = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=20, null=False, default='Anonymous')
    publish_date = models.DateTimeField(auto_now_add=True)
    address = models.FileField(null=False, upload_to=settings.ARTICLE_DIR)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-publish_date']