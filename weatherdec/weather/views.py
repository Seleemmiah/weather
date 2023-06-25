from django.http import HttpResponse

from django.shortcuts import render
import json
from datetime import datetime
import urllib.request

# Create your views here.
def index(request):
    try:
        # Handle POST request
        if request.method == 'POST':
            # Validate user input
            city = request.POST['city']
            current_time = datetime.now()
            formatted_time = current_time.strftime("%A, %B %d %Y, %H:%M:%S %p")
            res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=3aef2b5a71021258d219ee937aa77394').read()
            
            json_data = json.loads(res)
            data = {
                "city": city,
                "country_code": str(json_data['sys']['country']),
                "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
                "temp": 'Temperature: ' + str(json_data['main']['temp']) + ' °C ',
                "pressure": str(json_data['main']['pressure']),
                "humidity": 'Humidity: ' + str(json_data['main']['humidity']) + '%',
                "time": formatted_time
            }
        else:
            city = ''
            data = {}
        return render(request, 'index.html', {'city': city, 'data': data})
    
    except:
        return render(request, '404.html')
