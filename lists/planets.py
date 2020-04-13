##### Practice #####
planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")

new_planets = ["Uranus", "Neptune"]
planet_list.extend(new_planets)

planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")

planet_list.append("Pluto")

rocky_planets = planet_list[0:4]

del planet_list[-1:]

# print(rocky_planets)
# print(planet_list)

##### Challenge #####
spacecrafts = [
    ("Cassini", "Saturn"),
    ("Viking", "Mars")
]

for planet in planet_list:
    for key, value in spacecrafts:
        if value == planet:
            print(f'{key} spacecraft visited {planet}')