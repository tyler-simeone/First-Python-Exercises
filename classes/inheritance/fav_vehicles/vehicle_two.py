from vehicle import Vehicle

class Tesla(Vehicle):
    def __init__(self):
        self.battery_kwh = 0

    def drive(self):
        print(f"The {self.color} {self.model} drives past. Zoooooommm!")

    def turn(self, direction):
        print(f"The {self.model} turns {direction} on its own thanks to level 2 'hands-off' automation")