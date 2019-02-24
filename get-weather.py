#!/usr/bin/env python

import requests,subprocess,time

params = (
    ('q', 'ENTER-LOCATION-HERE'),
    ('appid', 'ENTER-API-KEY-HERE'),
)

while True:
    currenthour=int(time.strftime("%H"))
    if (currenthour >= 7) and (currenthour < 21):
        try:
            response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
        except requests.exceptions.RequestException as e:
            print(e)
        weatherCode = response.json().get('weather')[0].get('id')

        if weatherCode < 600:
            weatherIcon = 'rain.png'
        elif weatherCode < 700:
            weatherIcon = 'snow.png'
        elif weatherCode < 771:
            weatherIcon = 'fog.png'
        elif weatherCode < 782:
            weatherIcon = 'wind.png'
        elif weatherCode == 800:
            weatherIcon = 'clear-day.png'
        elif weatherCode < 804:
            weatherIcon = 'partly-cloudy-day.png'
        elif weatherCode == 804:
            weatherIcon = 'cloudy.png'

        subprocess.call(['python3', '/home/pi/unicorn-weather/weather-icons.py', weatherIcon])

    else:
        time.sleep(60)
