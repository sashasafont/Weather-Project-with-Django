from django.contrib import admin
from django.urls import path, include

app_name = "weather_app"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("weather_app.urls")),
]
