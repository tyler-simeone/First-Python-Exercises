from vehicle import Vehicle

# Vehicle class contains three properties that are shared among all
# classes below, as well as one 'drive' method
class Rivian(Vehicle):
    def __init__(self):
        self.battery_kwh = 0

class Tesla(Vehicle):
    def __init__(self):
        self.battery_kwh = 0

class Ford(Vehicle):
    def __init__(self):
        self.fuel_capacity = 0

class Porsche(Vehicle):
    def __init__(self):
        self.fuel_capacity = 0

class Ferrari(Vehicle):
    def __init__(self):
        self.fuel_capacity = 0