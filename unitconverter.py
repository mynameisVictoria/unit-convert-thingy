
class Convert:
	
	def __init__(self, celsius, kelvin, fahrenheit, rankine):
		self.celsius = celsius 
		self.kelvin = kelvin
		self.fahrenheit = fahrenheit
		self.rankine = rankine
		
	@staticmethod	
	def kelvin_to_celsius(kelvin):
		return kelvin - 273.15
		
	@staticmethod	
	def fahrenheit_to_celsius(fahrenheit):
		return (fahrenheit-32)/(9/5)
		
	@staticmethod	
	def rankine_to_celsius(rankine):
		return (rankine-491.67)*5/9
		
	@staticmethod
	def celsius_to_celsius(celsius):
		return celsius
	
	#-------------------------------------------------------------------------------#
	
	@staticmethod	
	def celsius_to_kelvin(celsius):
		return celsius + 273.15
		
	@staticmethod	
	def celsius_to_fahrenheit(celsius):
		return celsius*9/5+32
		
	@staticmethod	
	def celsius_to_rankine(celsius):
		return celsius*9/5 + 491.67
		
def test():
	print("hello world!")
	
