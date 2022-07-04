import random

import requests
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView
from .models import City
from .forms import CityForm


def index(request):
    appid = '57d518f0e3f1436269d961ca193ecfa7'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid


    if (request.method == 'POST'):

        global form
        form = CityForm(request.POST)
        form.save()
        return redirect('/')
    else:
        form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon'],
        }

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}
    return render(request, 'weather/index.html', context)


class DeletePosts(DeleteView):
    model = City
    form_class = CityForm
    template_name = "base.html"

