import requests
from bs4 import BeautifulSoup

def get_weather_data():
    
    url = 'https://yandex.ru/pogoda/moscow'
    response = requests.get(url)
    
    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')
        
        temperature = soup.find('span', class_='temp__value')
        if temperature:
            temperature = temperature.text
        else:
            temperature = "Температура не найдена"
        
        weather_condition = soup.find('div', class_='link__condition')
        if weather_condition:
            weather_condition = weather_condition.text
        else:
            weather_condition = "Состояние погоды не найдено"
        
        wind_info = soup.find('div', class_='wind-speed')
        if wind_info:
            wind_info = wind_info.text
        else:
            wind_info = "Информация о ветре не найдена"
        
        print(f"Температура: {temperature}")
        print(f"Состояние погоды: {weather_condition}")
        print(f"Ветер: {wind_info}")
    else:
        print(f"Ошибка при получении данных: {response.status_code}")

# Запускаем функцию
get_weather_data()