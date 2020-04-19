import datetime

class Building:
    def __init__(self, address, stories):
        self.designer = "Tyler"
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories
    
    def construct(self):
        self.date_constructed = datetime.datetime.now()

    def purchase(self, purchaser):
        self.owner = purchaser

    def print_description(self):
        print(f"{self.address} was purchased by {self.owner} on {self.date_constructed} and has {self.stories} stories \n")
