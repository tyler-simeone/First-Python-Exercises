from vehicle import Vehicle

class Ford(Vehicle):
    def __init__(self):
        self.fuel_capacity = 0

    def drive(self):
        print(f"The {self.color} {self.model} drives past. Vrooom!")