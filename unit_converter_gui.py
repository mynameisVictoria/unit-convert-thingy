from unitconverter import *
import tkinter as tk

root = tk.Tk()
root.geometry("300x500")

obj = Convert(0,0,0,0)

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
		
from_clicked = tk.StringVar()
to_clicked = tk.StringVar()

result_direction_label = tk.Label(root, text="this is the result, press return/enter")
result_direction_label.place(x=20, y=450)

direction_label = tk.Label(root, text="Bottom to top \n so if bottom is celsius and top is fahrenheit \n it will be, celsius -> fahrenheit", fg="black")
direction_label.place(x=10, y=80)

from_label = tk.Label(root, text="hello world!")
from_label.place(x=150, y=300)

to_label = tk.Label(root, text="hello world!")
to_label.place(x=150, y=200)

result_label = tk.Label(root, text="result_label")
result_label.place(x=20, y=430)

from_dropdown = tk.OptionMenu(root, from_clicked,  *options)
from_dropdown.place(x=20,y=300)

to_dropdown = tk.OptionMenu(root, to_clicked,  *options)
to_dropdown.place(x=20 ,y=200)

def from_show_func(event):
	
	from_label.config(text=from_clicked.get())
	to_label.config(text=to_clicked.get())
		
	if from_clicked.get() == "Celsius":
		celsius = obj.celsius_to_celsius(float(user_input.get()))
		if to_clicked.get()== "Celsius":
			result_label.config(text=round(obj.celsius_to_celsius(celsius)))
		elif to_clicked.get()=="Fahrenheit":
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
		
root.bind("<Return>", from_show_func)

root.mainloop()
