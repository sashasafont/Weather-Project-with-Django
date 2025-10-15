import os
import json
from django.core.management.base import BaseCommand
from weather_app.models import City, WeatherData

class Command(BaseCommand):
    help = "Importación de datos desde archivos .txt locales de AEMET (en la carpeta de backups)"
    
    def handle(self, *args, **kwargs):
        #ruta a la carpeta backups
        backups_path = os.path.join("weather_app", "backups")

        #comprobando si existe backups
        if not os.path.exists(backups_path):
            self.stdout.write(self.style.ERROR("Carpeta backups no encontrada"))
            return

        #pasando por cada carpeta dentro de backups
        for city_folder in os.listdir(backups_path):
            city_path = os.path.join(backups_path, city_folder)

            #ignorar archivos, dejar solo carpetas
            if not os.path.isdir(city_path):
                continue

            self.stdout.write(self.style.WARNING(f"Pensando en una ciudad: {city_folder}"))
            
            #objeto City
            city, _ = City.objects.get_or_create(
                name=city_folder.capitalize(),
                country="España"
            )

            #pasando por cada archivo txt
            for filename in os.listdir(city_path):
                if filename.endswith(".txt"):
                    file_path = os.path.join(city_path, filename)
                    self.stdout.write(self.style.NOTICE(f"Importando {filename}..."))
                    
                    #leer JSON del archivo txt
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            data = json.load(f)
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f"Error de lectura {filename}: {e}"))
                        continue

                    #revisamos cada elemento de dato (cada día)
                    for item in data:
                        #obtenemos los valores, si no estan establecer el valor predeterminado
                        temp = item.get("temperatura")
                        humidity = item.get("humedad")
                        description = item.get("description", "")

                        #omitir si no hay temperatura (campo obligatorio)
                        if temp is None:
                            continue

                        #crear o actualizar el registro
                        WeatherData.objects.update_or_create(
                            city=city,
                            date=item.get("fecha"),
                            defaults={
                                "temperature": temp,
                                "humidity": humidity if humidity is not None else 0,
                                "description": description,
                            },
                        )
            self.stdout.write(self.style.SUCCESS(f"Los datos de {city_folder} han sido importados"))