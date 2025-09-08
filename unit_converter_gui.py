from unitconverter import *
import tkinter as tk


root = tk.Tk()
root.geometry("500x500")

result_label = tk.Label(root, bg="black")
result_label.pack()

input_entry = tk.Entry(root, bg="black", fg="white")
input_entry.place(x=180, y=170)

obj_conver = Convert(0,0,0,0)

def from_kelvin():
	kelvin = input_entry.get()
	print(obj_conver.kelvin_to_celsius(round(float(kelvin))))
	

	




kelvin_btn = tk.Button(root, text="celsius", command=from_kelvin)
kelvin_btn.place(x=200,y=200)

root.mainloop()
