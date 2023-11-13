"""
Payden Schug
MO3 Lab.py
This program takes prompts the user for information about their vehicle and then stores the input data into a class. Once all the data has been collected it is printed out. The variables collected are
vehicle type(car), vehicle production year(year), vehicle manufacturer(make), vehicle model(model), vehicle door count(doors), and whether vehicle has a sunroof(roof). Error handling is done on doors
and roof to ensure a correct entry is present.

"""


class Vehicle:
    def __init__(self, car):
        self.car = car

class Automobile(Vehicle):
    def __init__(self, car, year, make, model, doors, roof):
        super().__init__(car)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

vehicle_type = Automobile(
input("Enter the vehicle type. \n"),
input("Enter the year your vehicle was made \n"),
input("Enter the make of your car \n"),
input("Enter the model of your car \n"),
input("Enter how many doors your vehicle has (2 or 4) \n"),
input("Enter whether your car has a sun roof('sun roof') or does not ('solid') \n"))

while vehicle_type.doors != '2' and vehicle_type.doors != '4':
    vehicle_type.doors = input("You have entered an incorrect amount of doors. Please either input a '2' for 2 doors or a '4' for 4 doors.\n")

while vehicle_type.roof != 'sun roof' and vehicle_type.roof != 'solid':
    vehicle_type.roof = input("You have entered an incorrect roof type. Please type 'sun roof' for a sun roof or 'solid' for no sun roof.\n")

print("Vehicle type: ", vehicle_type.car)
print("Year: ",vehicle_type.year)
print("Make: ", vehicle_type.make)
print("Model: ", vehicle_type.model)
print("Number of Doors: ", vehicle_type.doors)
print("Type of Roof: ", vehicle_type.roof)