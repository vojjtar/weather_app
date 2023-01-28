from django.shortcuts import render
from django.http import HttpResponse


def weather_index(request):

    city = 'kutna hora'
    api_key = ''

    geo_api = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={api_key}'


    context = {
        'city': 'kutna hora'
    }

    return render(request, 'weather/main_page.html', context=context)
