from vehicle import Vehicle

class Tesla(Vehicle):
    def __init__(self):
        self.battery_kwh = 0

    def drive(self):
        print(f"The {self.color} {self.model} drives past. Zoooooommm!")