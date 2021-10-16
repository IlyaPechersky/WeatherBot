import requests
import datetime
from config import open_weather_token
from pprint import pprint


def get_weather(city: str, open_weather_token: str):

    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        # pprint(data)

        city = data["name"]
        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно, не понимаю, что там("
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        return (f"Погода в городе {city}: \n"
              f"- {wd}\n"
              f"- температура {cur_weather} °C\n"
              f"- влажность {humidity}%\n- давление {pressure} мм.рт.ст.\n"
              f"- скорость ветра {wind} м/с\n"
              f"- время восхода {sunrise_timestamp}\n"
              f"- время заката {sunset_timestamp}\n"
              f"Хорошего дня!")

    except Exception as ex:
        print(ex)
        return f"{ex}\nПроверьте входные данные"

def main():
    city = input("Введите город: ")
    get_weather(city.lower(), open_weather_token)

if __name__ == "__main__":
    main()