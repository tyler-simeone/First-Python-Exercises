zoo = ("shi-tzu", "black lab", "monkey", "cheetah")

print(zoo.index("shi-tzu"))

animal_to_find = "shi-tzu"
if animal_to_find in zoo:
    print("animal found!")

(tylers_pet, sams_pet, zoo_animal, african_animal) = zoo
print(tylers_pet)
print(sams_pet)
print(zoo_animal)
print(african_animal)

zoo_as_list = list(zoo)
print(type(zoo_as_list))

more_animals = ["kangaroo", "shark", "deer"]
zoo_as_list.extend(more_animals)
print(zoo_as_list)

zoo_back_to_tuple = tuple(zoo_as_list)
print(type(zoo_back_to_tuple))