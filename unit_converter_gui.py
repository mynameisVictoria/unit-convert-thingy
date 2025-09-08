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
	
def from_show():
	from_label.config(text=from_clicked.get())
	celsius = obj.celsius_to_celsius(float(user_input.get()))
	if from_clicked.get() == "Celsius":
		if to_clicked == "Celsius":
			print(text=obj.celsius_to_celsius(celsius))
			
		elif to_clicked == "Fahrenheit":
			treturn

from_clicked = tk.StringVar()
to_clicked = tk.StringVar()


from_label = tk.Label(root, text="hello world!")
from_label.place(x=400, y=300)

to_label = tk.Label(root, text="hello world!")
to_label.place(x=400, y=200)

result_label = tk.Label(root, text="hello world!")
result_label.pack()

from_dropdown = tk.OptionMenu(root, from_clicked,  *options)
from_dropdown.place(x=150,y=300)

to_dropdown = tk.OptionMenu(root, to_clicked,  *options)
to_dropdown.place(x=150 ,y=200)

myButton = tk.Button(root, text="comfirm", command=from_show).place(x=300, y=300)


root.mainloop()
