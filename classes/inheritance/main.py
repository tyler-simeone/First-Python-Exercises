from fav_vehicles import Rivian, Tesla, Porsche, Ford, Ferrari

rivian_pickup = Rivian()
rivian_pickup.color = "Blue"
rivian_pickup.maximum_occupancy = "5"
rivian_pickup.model = "Rivian R1T"
rivian_pickup.battery_kwh = 180

rivian_pickup.drive()

ford_f150 = Ford()
ford_f150.color = "Black"
ford_f150.maximum_occupancy = "5"
ford_f150.model = "Ford 150"
ford_f150.fuel_capacity = 36

ford_f150.drive()

ferrari_458 = Ferrari()
ferrari_458.color = "Dark Red"
ferrari_458.maximum_occupancy = "2"
ferrari_458.model = "Ferrari 458 Speciale"
ferrari_458.fuel_capacity = 23

ferrari_458.drive()

tesla_modelS = Tesla()
tesla_modelS.color = "Black"
tesla_modelS.maximum_occupancy = "5"
tesla_modelS.model = "Tesla Model S P100D"
tesla_modelS.battery_kwh = 100

tesla_modelS.drive()

porsche_gt3 = Porsche()
porsche_gt3.color = "White"
porsche_gt3.maximum_occupancy = "2"
porsche_gt3.model = "Porsche 911 GT3RS"
porsche_gt3.fuel_capacity = 17

porsche_gt3.drive()

