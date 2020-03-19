from Car import Car

class ParkingPosition(object):
	"""docstring for ParkingPosition"""
	def __init__(self, number):
		self.__spot_number = number
		self.__is_occupied = False
		self.__car = None

	def is_occupied(self) -> bool:
		return self.__is_occupied

	def set_car(self, car) -> None:
		self.__car = car
		self.__is_occupied = True

	def get_car(self) -> Car:
		return self.__car

	def remove_car(self) -> None:
		self.__car = None
		self.__is_occupied = False
