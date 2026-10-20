import requests
import random
from tkinter import *

# Задание 1
api_key1 = 'aa7f8bf35f4eb5c895d53d2cc08f2a45'

def get_weather(city_name, api_key):
    

    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric',
        'lang': 'ru'
    }

    response = requests.get(url=base_url, params=params)
    response = response.json()
    return response

# city_name = input("Введите название города:")
# weather = get_weather(city_name, api_key1)
# print(f"Погода: {weather['main']['temp']}°C\nВлажность: {weather['main']['humidity']}%\nДавление: {weather['main']['pressure']}гПа")

# Задание 2

base_url = "https://rickandmortyapi.com/api/character/1"

params = {
    "name": "Rick Sanchez",
    "status": "alive"
}

get = requests.get(url=base_url, params=params)
response = get.json()
# print(f"Имя персонажа: {response['name']}")
# print(f"ID персонажа: {response['id']}")
# print(f"Гендер персонажа: {response['gender']}")
# print(f"Тип персонажа: {response['species']}")
# print(f"Статус персонажа: {response['status']}")

# Допзадание

# base_url_dop = 'https://nekos.best/api/v2'


# root = Tk()
# root.title('Генератор картинок')
# root.geometry('500x500')
# btn = Button(root, text='Сгенерировать картинку')
# btn.place(relx=0.33, rely=0.8)


# root.mainloop()