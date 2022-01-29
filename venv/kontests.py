import tkinter as tk
from datetime import datetime

import requests
import time


def getEvents(canvas):
    api = "https://kontests.net/api/v1/all"
    json_data = requests.get(api).json()
    name = json_data['name']
    url = json_data['url']

    final_info = "These are the events and links"
    final_data = "\n" + name+ "\n" + url

    label1.config(text=final_info)
    label2.config(text=final_data)





# //define UI

canvas = tk.Tk()
# set geometry of canvas
canvas.geometry("600x500")
canvas.title("Events Coding")

# fonts
f = ("poppins", 15, "bold")
t = ("poppins", 22, "bold")

# # get text city from user and attach to canvas
# textfield = tk.Entry(canvas, justify='center', font=t)
# textfield.pack(pady=20)
# textfield.focus()
#
# # attach entered city to collect weather data for that city
#
# textfield.bind('<Return>', getEvents)
# attach to canvas
label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()
