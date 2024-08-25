import requests
from django.shortcuts import render

# Create your views here.
def weather_view(request):
    api_key = 'aaca84984ee7ffa0f4d5d7833b03a7c6'
    city = 'Rio de Janeiro'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(url)
    weather_data = response.json()

    if response.status_code == 200:  # Verifique se a requisição foi bem-sucedida
        context = {
            'city': weather_data.get('name', 'Unknown location'),  # Use `.get()` para evitar KeyError
            'temperature': weather_data['main'].get('temp', 'No data'),
            'description': weather_data['weather'][0].get('description', 'No data'),
            'icon': weather_data['weather'][0].get('icon', ''),
        }
    else:
        context = {
            'city': 'Error fetching data',
            'temperature': 'N/A',
            'description': 'N/A',
            'icon': '',
        }

    return render(request, 'weather_app/weather.html', context)