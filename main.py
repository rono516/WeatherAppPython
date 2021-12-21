# import datetime
# today = datetime.datetime.now()
# date_time = today.strftime("%H:%M:%S")
# print("Today and now is: ", date_time)

import tkinter as tk
import requests
import time

# define UI
canvas = tk.Tk()
canvas.geometry("650x500")
canvas.title("Rono's App")

# get text from user
textfield = tk.Entry(canvas, justify="center")


def getweather():
    city = textfield.get()
    api = ""
    json_data = requests.get(api).json()

    condition = json_data['weather']['0']['main']
    condition_description = json_data['weather']['description']
    temp = int(json_data['main']['temp'] - 273.25)
    min_temp = json_data['main']['temp_min']
    max_temp = json_data['main']['temp_max']
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise']-10800))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset']-10800))
