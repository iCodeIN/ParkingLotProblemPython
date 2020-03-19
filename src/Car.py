class Car(object):
	"""docstring for Car"""
	def __init__(self, registration_number, color):
		self.__registration_number = registration_number
		self.__color = color

	def get_registration_number(self):
		return self.__registration_number

	def get_color(self):
		return self.__color

