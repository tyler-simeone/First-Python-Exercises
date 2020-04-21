from vehicle import Vehicle

class Porsche(Vehicle):
    def __init__(self):
        self.fuel_capacity = 0

    def drive(self):
        print(f"The {self.color} {self.model} drives past. Vrooooom!")

    def stop(self):
        print(f"The {self.model} quickly comes to a stop thanks to powerful carbon-ceramic disc brakes.")