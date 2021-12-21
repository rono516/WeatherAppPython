import tkinter as tk
from datetime import datetime

import requests
import time


def getWeather(canvas):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=3d9da6ab4fe75139d5432c89d316a744"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)

    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)

    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']

    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 10800))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 10800))

    final_info = "The overall condition of " + city + " is " + condition + "\n" + "Temperature at " + str(temp) + "°C"
    final_data = "\n" + "Maximum Temperature: " + str(max_temp) + "\n" + "Minimum Temperature: " + str(
        min_temp) + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(
        humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + "\n" + sunrise + "Sunset: " + sunset

    label1.config(text=final_info)
    label2.config(text=final_data)


# //define UI

canvas = tk.Tk()
# set geometry of canvas
canvas.geometry("600x500")
canvas.title("Weather According to Cities")

# fonts
f = ("poppins", 15, "bold")
t = ("poppins", 22, "bold")

# get text city from user and attach to canvas
textfield = tk.Entry(canvas, justify='center', font=t)
textfield.pack(pady=20)
textfield.focus()

# attach entered city to collect weather data for that city

textfield.bind('<Return>', getWeather)
# attach to canvas
label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()
