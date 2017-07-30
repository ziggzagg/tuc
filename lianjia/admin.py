# -*- coding: utf-8 -*-

from django.contrib import admin
from models import Website, SoldFlat
# Register your models here.


def decode(info):
    return info.decode('utf-8')


class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'url_',
                    'scraper')
    list_display_links = ('name',)

    def url_(self, instance):
        return '<a href="{url}" target="_blank">{title}</a>'.format(
            url=instance.url, title=instance.url)
    url_.allow_tags = True


class SoldFlatAdmin(admin.ModelAdmin):
    list_display = ('id',
                    # 'title',
                    'address',
                    'size',
                    'n_livingroom',
                    'n_bedroom',
                    'district',
                    'region',
                    # 'floor',
                    'age',
                    'sold_date',
                    'average_price',
                    'total_price',
                    'website',
                    'url_',
                    )
    list_display_links = ('address',)
    raw_id_fields = ('checker_runtime',)

    def url_(self, instance):
        return '<a href="{url}" target="_blank">{title}</a>'.format(
            url=instance.url, title=instance.url)
    url_.allow_tags = True

admin.site.register(Website, WebsiteAdmin)
admin.site.register(SoldFlat, SoldFlatAdmin)

