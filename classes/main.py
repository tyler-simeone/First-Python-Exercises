from building import Building
from city import City

# Creating a new city instance
megtropolis = City("Megtropolis", "Rob Downey Jr")

#### Creating buildings for our new city ####
batman_building = Building("123 main st", 20)
batman_building.purchase("Real estate company")
batman_building.construct()
# batman_building.print_description()

renaissance_hotel = Building("400 Carothers Blvd", 9)
renaissance_hotel.purchase("Big Brothers Group")
renaissance_hotel.construct()
# renaissance_hotel.print_description()


capital_building = Building("12 Capital Blvd", 4)
capital_building.purchase("Git-Er-Done Real Estate Group")
capital_building.construct()
# capital_building.print_description()


regions_bank = Building("8088 Regions Blvd", 3)
regions_bank.purchase("Financial Real Estate Group")
regions_bank.construct()
# regions_bank.print_description()


empire_state = Building("20 W 34th St, New York, NY 10001", 102)
empire_state.purchase("Capital Investments")
empire_state.construct()
# empire_state.print_description()

# Adding the buildings to our new city
megtropolis.add_building(batman_building, renaissance_hotel, capital_building, regions_bank, empire_state)

for building in megtropolis.buildings:
    # So I can print the individual properties of each building obj, 
    # but I can't print a list of its key/value pairs...
    print(f"Address: {building.address}, Stories: {building.stories}")
