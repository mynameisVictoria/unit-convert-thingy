from unit_converter_backend import *
import tkinter as tk

root = tk.Tk()
root.geometry("340x700")

obj = Convert(0, 0, 0, 0)

user_input = tk.Entry(root, width=25)
user_input.place(x=20, y=150)

root.title("Unit Conversion Program")

easter_egg = tk.Label(root, text="lmao")
easter_egg.place(x=600, y=600)

options = [
    "Celsius",
    "Fahrenheit",
    "Kelvin",
    "Rankine"
    ]

options_length = [
    "Millimeter",
    "Centimeter",
    "Decimeter",
    "Meter",
    "Inch",
    "Foot",
    "Yard",
    "Mile"
    ]

from_clicked = tk.StringVar()
to_clicked = tk.StringVar()

from_clicked_length = tk.StringVar()
to_clicked_length = tk.StringVar()

result_direction_label = tk.Label(root, text="______________________ \n"
                                             "Press return/enter")
result_direction_label.place(x=20, y=430)

direction_label = tk.Label(root,
                           text="Bottom to top \n so if bottom is celsius and top is fahrenheit \n it will be, celsius -> fahrenheit",
                           fg="black")

direction_label.place(x=10, y=80)
from_label = tk.Label(root, text="Converts this")
from_label.place(x=150, y=300)
to_label = tk.Label(root, text="To this")
to_label.place(x=150, y=200)
result_label = tk.Label(root, text="")
result_label.place(x=20, y=420)
from_dropdown = tk.OptionMenu(root, from_clicked, *options)
from_dropdown.place(x=20, y=300)
to_dropdown = tk.OptionMenu(root, to_clicked, *options)
to_dropdown.place(x=20, y=200)

from_dropdown_length = tk.OptionMenu(root, from_clicked_length, *options_length)
to_dropdown_length = tk.OptionMenu(root, to_clicked_length, *options_length)
from_dropdown_length.place(x=20, y=500)
to_dropdown_length.place(x=20, y=600)


def from_show_func(event):
    from_label.config(text=from_clicked.get())
    to_label.config(text=to_clicked.get())

    if from_clicked.get() == "Celsius":
        celsius = obj.celsius_to_celsius(float(user_input.get()))
        if to_clicked.get() == "Celsius":
            result_label.config(text=round(obj.celsius_to_celsius(celsius)))
        elif to_clicked.get() == "Fahrenheit":
            result_label.config(text=round(obj.celsius_to_fahrenheit(celsius)))
        elif to_clicked.get() == "Kelvin":
            result_label.config(text=round(obj.celsius_to_kelvin(celsius)))
        elif to_clicked.get() == "Rankine":
            result_label.config(text=round(obj.celsius_to_rankine(celsius)))

    elif from_clicked.get() == "Fahrenheit":
        celsius = obj.fahrenheit_to_celsius(float(user_input.get()))
        if to_clicked.get() == "Fahrenheit":
            result_label.config(text=round(obj.celsius_to_fahrenheit(celsius)))
        elif to_clicked.get() == "Celsius":
            result_label.config(text=round(obj.celsius_to_celsius(celsius)))
        elif to_clicked.get() == "Kelvin":
            result_label.config(text=round(obj.celsius_to_kelvin(celsius)))
        elif to_clicked.get() == "Rankine":
            result_label.config(text=round(obj.celsius_to_rankine(celsius)))

    elif from_clicked.get() == "Kelvin":
        celsius = obj.kelvin_to_celsius(float(user_input.get()))
        if to_clicked.get() == "Fahrenheit":
            result_label.config(text=round(obj.celsius_to_fahrenheit(celsius)))
        elif to_clicked.get() == "Celsius":
            result_label.config(text=round(obj.celsius_to_celsius(celsius)))
        elif to_clicked.get() == "Kelvin":
            result_label.config(text=round(obj.celsius_to_kelvin(celsius)))
        elif to_clicked.get() == "Rankine":
            result_label.config(text=round(obj.celsius_to_rankine(celsius)))

    elif from_clicked.get() == "Rankine":
        celsius = obj.rankine_to_celsius(float(user_input.get()))
        if to_clicked.get() == "Fahrenheit":
            result_label.config(text=round(obj.celsius_to_fahrenheit(celsius)))
        elif to_clicked.get() == "Celsius":
            result_label.config(text=round(obj.celsius_to_celsius(celsius)))
        elif to_clicked.get() == "Kelvin":
            result_label.config(text=round(obj.celsius_to_kelvin(celsius)))
        elif to_clicked.get() == "Rankine":
            result_label.config(text=round(obj.celsius_to_rankine(celsius)))

    if from_clicked_length.get() == ""


root.bind("<Return>", from_show_func)

root.mainloop()
