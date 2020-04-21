from vehicle import Vehicle

# Vehicle class contains three properties that are shared among all
# classes below, as well as one 'drive' method
class Rivian(Vehicle):
    def __init__(self):
        super().__init__()
        self.battery_kwh = 0

    def drive(self):
        print(f"The {self.color} {self.model} drives past. Zoooooommm!")