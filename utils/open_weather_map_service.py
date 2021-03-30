import requests as reqs

def get_outside_temp():
    data = {}
    url = 'https://api.openweathermap.org/data/2.5/weather?id=2648579&appid=ab3b10ceeb32e9e2635906ef718eec7f&units=metric'
    response = reqs.get(url, data)
    return response.json()['main']['temp']

def get_outside_feels_like_temperature():
    data = {}
    url = 'https://api.openweathermap.org/data/2.5/weather?id=2648579&appid=ab3b10ceeb32e9e2635906ef718eec7f&units=metric'
    response = reqs.get(url, data)
    return response.json()['main']['feels_like']