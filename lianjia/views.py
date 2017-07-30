from datetime import date

from dateutil.relativedelta import relativedelta
from django.db.models import Count
from django.http import JsonResponse
from django.views.generic import TemplateView

from models import SoldFlat


# Create your views here.


# base class
class SoldFlatCount(TemplateView):
    template_name = 'lianjia/index.html'

    def get_context_data(self, **kwargs):
        context = super(SoldFlatCount, self).get_context_data(**kwargs)
        key = 'last-30-days'
        results = get_internal(key)
        context['sold_flat_date'] = results['sold_flat_date']
        context['sold_flat_count'] = results['sold_flat_count']
        return context


def fetch_ajax(request, key):
    return JsonResponse(get_internal(key))


def get_internal(key):
    filter_switcher = {
        "last-30-days": relativedelta(days=30),
        "last-90-days": relativedelta(days=90),
        "last-180-days": relativedelta(days=180),
        "last-360-days": relativedelta(days=360),
    }
    filter_delta = filter_switcher.get(key, relativedelta(days=30))
    filter_results = SoldFlat.objects \
        .values('sold_date') \
        .filter(sold_date__range=[date.today() - filter_delta, date.today()]) \
        .order_by('sold_date')

    step_switcher = {
        "last-30-days": relativedelta(days=1),
        "last-90-days": relativedelta(days=10),
        "last-180-days": relativedelta(days=15),
        "last-360-days": relativedelta(days=30),
    }
    step_delta = step_switcher.get(key, relativedelta(days=1))

    results = []
    start = filter_results[0]['sold_date']
    end = date.today() - relativedelta(days=15)
    while start <= end:
        split = filter_results \
            .filter(sold_date__range=[start, start + step_delta]) \
            .count()
        start = start + step_delta
        results.append({'sold_date': start.strftime('%Y/%m/%d'), 'count': split})

    sold_flat_count = map(lambda i: i['count'], results)
    sold_flat_date = map(lambda i: i['sold_date'], results)
    return {"sold_flat_count": sold_flat_count, "sold_flat_date": sold_flat_date}