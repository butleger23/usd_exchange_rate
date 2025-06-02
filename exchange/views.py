import requests

from django.http import HttpResponse, JsonResponse
from django_ratelimit.decorators import ratelimit

from .models import USDExchangeRate


def get_exchange_rate():
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    response.raise_for_status()
    data = response.json()
    exchange_rate = data['Valute']['USD']['Value']
    USDExchangeRate.objects.create(exchange_rate=exchange_rate)

    return exchange_rate


@ratelimit(key='ip', rate='1/10s')
def get_current_usd(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    current_rate = get_exchange_rate()
    last_10_rates = USDExchangeRate.objects.order_by('-timestamp')[0:10]

    rates_data = [
        {'exchange_rate': str(rate.exchange_rate), 'timestamp': rate.timestamp}
        for rate in last_10_rates
    ]

    response_data = {
        'current_rate': str(current_rate) if current_rate else None,
        'last_10_rates': rates_data,
    }

    return JsonResponse(response_data)


def rate_limited_view(request, exception):
    return HttpResponse(
        'Rate limit exceeded. Please try again later.',
        status=429,
        content_type='text/plain',
    )
