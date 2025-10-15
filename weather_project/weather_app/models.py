from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True)
    role = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username
    
class Event(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='events') #OneToMany
    description = models.TextField(blank=True)
    date_start = models.DateField()
    date_end = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=200, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='events') #ManyToMany

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('weather_app:event_detail', kwargs={'pk': self.pk})
    
class Record(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='records') #OneToMany
    date = models.DateField()
    temperature = models.FloatField(null=True, blank=True)
    humidity = models.FloatField(null=True, blank=True)
    note = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.event.title} - {self.date}"

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