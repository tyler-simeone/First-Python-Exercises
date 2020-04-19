class City:
    def __init__(self, cityname, mayor):
        self.city_name = cityname
        self.mayor = mayor
        self.year_established = ""
        self.buildings = list()

    # can pass in list of >= 1 building argument
    def add_building(self, *aargs):
        self.buildings.extend(aargs)
