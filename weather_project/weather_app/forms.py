from django import forms
from .models import Event, Record, Category, City
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['date', 'temperature', 'humidity', 'note']
        widgets = {'date': forms.DateInput(attrs={'type':'date'})}

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", max_length=100)
    email = forms.EmailField(label="Correo electrónico")
    comment = forms.CharField(label="Comentario", widget=forms.Textarea)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class AddCityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ["name", "country"]
        labels = {
            "name": "Nombre de la ciudad/pueblo",
            "country": "Provincia",
        }