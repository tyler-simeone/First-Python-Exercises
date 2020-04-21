class Vehicle:
    def __init__(self):
        self.color = ""
        self.maximum_occupancy = ""
        self.model = ""
    
    def drive(self):
        print("Vrooom!")

    def turn(self, direction):
        print(f"Turning {direction}")

    def stop(self):
        print("Stopping")