my_family = {
    "dad": {
        "name": "Chris",
        "age": 59
    },
    "mom": {
        "name": "Lisa",
        "age": 57
    }
}

# **** This one was interesting, I learned that in an f string, if accessing a dictionary's string property name, need to use single quotes bc already using doubles.

family_string = [f"{value['name']} is my {key} and is {str(value['age'])} years old." for key, value in my_family.items()]
print(family_string)