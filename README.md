# unicorn-weather
Weather icon system for the Pimoroni Unicorn HAT

weather-icons.py and icons/* (C) 2016 LoveBootCaptain, MIT Licence
get-weather.py (C) 2019 Gareth Halfacree, BSD 3-Clause Licence

Downloads weather data from OpenWeatherMap, displays it on a connected Pimoroni UnicornHAT.

Setup:
$ sudo python -m pip install unicornhat requests pillow

Notes:
Only runs from 0700 to 2100 (so you're not blinded at night.)
Loops inifinitely.
Fairly gross handling of OWM's various condition codes.
Requires 'requests' Python library.
