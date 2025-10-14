from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.name}, {self.country}" if self.country else self.name

class WeatherData(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    date = models.DateField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"El tiempo en {self.city.name} el día {self.date}: {self.temperature}°C, {self.humidity}%, {self.description}"