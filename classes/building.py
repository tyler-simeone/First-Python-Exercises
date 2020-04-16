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

batman_building = Building("123 main st", 20)
batman_building.purchase("Real estate company")
batman_building.construct()
batman_building.print_description()

renaissance_hotel = Building("400 Carothers Blvd", 9)
renaissance_hotel.purchase("Big Brothers Group")
renaissance_hotel.construct()
renaissance_hotel.print_description()


capital_building = Building("12 Capital Blvd", 4)
capital_building.purchase("Git-Er-Done Real Estate Group")
capital_building.construct()
capital_building.print_description()


regions_bank = Building("8088 Regions Blvd", 3)
regions_bank.purchase("Financial Real Estate Group")
regions_bank.construct()
regions_bank.print_description()


empire_state = Building("20 W 34th St, New York, NY 10001", 102)
empire_state.purchase("Capital Investments")
empire_state.construct()
empire_state.print_description()