class ParkingLot(object):
	"""docstring for ParkingLot"""

	instance = None
	
	class __singleton:
		def __init__(self, size):
			self.__size = size
			self.__slots = []
			self.__registered_cars = {}

	def __init__(self, size):
		if (int(size) < 0):
			print("Please enter a valid parking lot size")
			return

		if not ParkingLot.instance:
			ParkingLot.instance = ParkingLot.__singleton(int(size))
		else:
			ParkingLot.instance.size = int(size)

		for i in range(int(size)):
				ParkingLot.instance.__slots.append(ParkingPosition(i+1))

		print("Successfully created a new parking lot with #{size} slots")


	def get_size(self) -> int:
		return self.__size

	def get_slots(self) -> []:
		return self.__slots 

	def get_registered_cars(self) -> {}:
		return self.__registered_cars

	def park(self, registration_number, color):
		empty_spot = 0
		for i in range(len(ParkingLot.instance.__size)):
			if ParkingLot.instance.__slots[i].is_occupied() == False:
				empty_spot = i+1
				break
		if(empty_spot == 0):
			print("Sorry, Parking is full. Please come back later!")
		else:
			current_slot = ParkingLot.instance.__slots[empty_spot]
			print("Allocated slot number: #{empty_spot}")

			if ParkingLot.instance.__registered_cars.get(registration_number) is not None:
				current_slot.car = ParkingLot.instance.__registered_cars.get(registration_number)
				ParkingLot.instance.__registered_cars.get(registration_number).set_spot(current_slot)
			else:
				car = Car(registration_number, color)
				current_slot.set_car(car)
				car.set_spot(current_slot)
				ParkingLot.instance.__registered_cars[registration_number] = car





		
		