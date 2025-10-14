from django import forms
from .models import City

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", max_length=100)
    email = forms.EmailField(label="Correo electrónico")
    comment = forms.CharField(label="Comentario", widget=forms.Textarea)

class AddCityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ["name", "country"]
        labels = {
            "name": "Nombre de la ciudad/pueblo",
            "country": "Provincia",
        }