

class Convert:
	
	def __init__(self, celsius, kelvin, fahrenheit, rankine):
		self.celsius = celsius 
		self.kelvin = kelvin
		self.fahrenheit = fahrenheit
		self.rankine = rankine
		
	def kelvin_to_celsius(self, kelvin):
		self.kelvin = kelvin
		return self.kelvin - 273.15
	def fahrenheit_to_celsius(self, fahrenheit):
		self.fahrenheit = fahrenheit
		return (fahrenheit-32)/(9/5)
	def rankine_to_celsius(self, rankine):
		self.rankine = rankine 
		return (rankine-491.67)*5/9
	#-------------------------------------------------------------------------------#
	
	def celsius_to_kelvin(self, celsius):
		self.celsius = celsius
		return celsius + 273.15
	
conversion_obj  = Convert(0,0,0,0)

from_input = str(input(""))
to_input = str(input(""))
num_input = float(input(""))

if "K" in from_input:
	celsius = conversion_obj.kelvin_to_celsius(num_input)
	if to_input == "K":
		print(round(conversion_obj.celsius_to_kelvin(celsius)))
		

elif "F" in from_input:
	celsius = conversion_obj.fahrenheit_to_celsius(num_input)
	if to_input == "K":
		print(round(conversion_obj.celsius_to_kelvin(celsius)))

elif "R" in from_input:
	celsius = conversion_obj.rankine_to_celsius(num_input)
	if to_input == "K":
		print(round(conversion_obj.celsius_to_kelvin(celsius)))
		
		
		
	



		
		
		
	
		
