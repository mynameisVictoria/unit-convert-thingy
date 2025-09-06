import tkinter as tk

root = tk.Tk()
root.geometry("500x500")

entry = tk.Entry(root)
entry.place(x=150, y=400)

conversion_label = tk.Label(root, bg="black", text="hello world", fg="white")
conversion_label.place(x=200, y=200)

unit_label = tk.Label(root,bg="black", fg="white", text="hello world")
unit_label.place(x=200, y=230)

class convert_celsius_fahrenheit:
		def __init__(self, celsius, fahrenheit ):
			self.celsius = celsius
			self.fahrenheit = fahrenheit
			
		def fahrenheit_to_celsius(self, fahrenheit):
			self.fahrenheit = fahrenheit
			
			self.fahrenheit = float(self.fahrenheit) - 32
			self.fahrenheit = float(self.fahrenheit)/1.8 

			conversion_label.config(text=(round(float(self.fahrenheit))))
			
		def celsius_to_fahrenheit(self, celsius):
			self.celsius = celsius
			
			self.celsius = float(self.celsius)*1.8
			self.celsius = float(self.celsius) + 32
			
			conversion_label.config(text=(round(float(self.celsius))))
		
#-------------------------------------------------------------------------------------------------------# <-- key handling and gui handling mostly

def celsius_buttom_cmd():
	global celsius_true

	celsius_true = True
	unit_label.config(text="fahrenheit to celsius")
def fahrenheit_buttom_cmd():
	global celsius_true
	
	celsius_true = False 
	unit_label.config(text="celsius to fahrenheit")


celsius_button = tk.Button(root, text="celsius",command=celsius_buttom_cmd)
fahrenheit_button = tk.Button(root, text="fahrenheit",command=fahrenheit_buttom_cmd)

celsius_button.place(x=100, y=100)
fahrenheit_button.place(x=100, y=130)

def enter_press(event):
	
	conversion_value = entry.get()
	conversion_obj = convert_celsius_fahrenheit(0, 0)
		
	if celsius_true == True:
		conversion_obj.fahrenheit_to_celsius(conversion_value)
	elif celsius_true == False:
		conversion_obj.celsius_to_fahrenheit(conversion_value)

root.bind("<Return>", enter_press)

root.mainloop()

