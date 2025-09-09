from unitconverter import *
import tkinter as tk


root = tk.Tk()
root.geometry("500x500")

obj = Convert(0,0,0,0)

user_input = tk.Entry(root)
user_input.pack()
	
options = [  
	"Celsius", 
	"Fahrenheit",
	"Kelvin",
	"Ronkine"
	]
		

from_clicked = tk.StringVar()
to_clicked = tk.StringVar()

from_label = tk.Label(root, text="hello world!")
from_label.place(x=400, y=300)

to_label = tk.Label(root, text="hello world!")
to_label.place(x=400, y=200)

result_label = tk.Label(root, text="result_label")
result_label.pack()

from_dropdown = tk.OptionMenu(root, from_clicked,  *options)
from_dropdown.place(x=150,y=300)

to_dropdown = tk.OptionMenu(root, to_clicked,  *options)
to_dropdown.place(x=150 ,y=200)

def from_show_func(event):
	
	from_label.config(text=from_clicked.get())
	to_label.config(text=to_clicked.get())
		
	if from_clicked.get() == "Celsius":
		celsius = obj.celsius_to_celsius
		if to_clicked == "Celsius":
			print(obj.celsius_to_celsius(celsius))
			
	elif from_clicked == "Fahrenheit":
		fahrenheit = obj.fahrenheit_to_celsius(user_input.get())
		if to_clicked == "Fahrenheit":
			print(obj.celsius_to_fahrenheit(fahrenheit))
		
root.bind("<Return>", from_show_func)



root.mainloop()
