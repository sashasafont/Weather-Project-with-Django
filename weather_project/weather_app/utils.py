import requests
from .models import City, WeatherData
from datetime import datetime

API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJzYWZvbnRzYW5la0BnbWFpbC5jb20iLCJqdGkiOiJiYjY0MDVkYi02NjY0LTQ0OTctYThmYy1jZjEzNWFlN2M5NzMiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTc1OTkzMzE3MywidXNlcklkIjoiYmI2NDA1ZGItNjY2NC00NDk3LWE4ZmMtY2YxMzVhZTdjOTczIiwicm9sZSI6IiJ9.UClfyTnrccdRTBV0QB_Nng3oxAMBmPqK8dIofyWrvIs"

def fetch_weather_data(city_code):
    print(f"Iniciando la función para el código de ciudad: {city_code}")

    url = f"https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/diaria/{city_code}/?api_key={API_KEY}"
    response = requests.get(url)
    print(f"Código de estado de la petición: {response.status_code}")

    if response.status_code != 200:
        print(f"Error al obtener datos para el código de ciudad {city_code}")
        return
    
    data_url = response.json().get('datos')
    print(f"URL de datos recibido: {data_url}")

    if not data_url:
        print(f"No se encontró ninguna URL de datos para el código de ciudad {city_code}")
        return

    weather_json = requests.get(data_url).json()
    print(f"Primeros datos descargados del JSON: {weather_json[:1]}")

    today_forecast = weather_json[0]['prediccion']['dia'][0]

    description = ""
    for estado in today_forecast['estadoCielo']:
        if estado['descripcion']:
            description = estado['descripcion']
            break

    temperature = today_forecast['temperatura']['maxima']
    humidity = today_forecast.get("humedadRelativa", {}).get('maxima', 0)

    city_name = weather_json[0]['nombre']
    province = weather_json[0]['provincia']
    city, _ = City.objects.get_or_create(name=city_name, country=province)

    WeatherData.objects.create(
        city=city,
        date=datetime.now().date(),
        temperature=temperature,
        humidity=humidity,
        description=description
    )

    print(f"Datos meteorológicos guardados para {city_name}")