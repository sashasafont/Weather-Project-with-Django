from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import City, WeatherData
from .forms import ContactForm
from .forms import ContactForm, AddCityForm

def home(request):
    return render(request, "weather_app/home.html")

class CityListView(ListView):
    model = City
    template_name = "weather_app/city_list.html"
    context_object_name = "cities"

class WeatherListView(ListView):
    model = WeatherData
    template_name = "weather_app/weather_list.html"
    context_object_name = "weathers"

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect("weather_app:thanks")
    else:
        form = ContactForm()
    return render(request, "weather_app/contact.html", {"form": form})

def thanks(request):
    return render(request, "weather_app/thanks.html")

def add_city(request):
    if request.method == "POST":
        form = AddCityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("weather_app:city_list")
    else:
        form = AddCityForm()

    return render(request, "weather_app/add_city.html", {"form": form})