from django.urls import path
from . import views

app_name = "weather_app"

urlpatterns = [
    path("", views.home, name="home"),
    path("cities/", views.CityListView.as_view(), name="city_list"),
    path("weather/", views.WeatherListView.as_view(), name="weather_list"),
    path("contact/", views.contact, name="contact"),
    path("thanks/", views.thanks, name="thanks"),
    path("add_city/", views.add_city, name="add_city"),
]