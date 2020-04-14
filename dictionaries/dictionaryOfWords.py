#### Practice 1 ####
"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions["Pizza"] = "Italian heritage, round shaped dough with red sauce and cheese traditionally."
word_definitions["Apple"] = "Healthy fruit with fiber, antioxidants, and prebiotics for the gut."
word_definitions["Banana"] = "Healthy fruit with potassium and a good source of prebiotics for the gut"

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
pizza_definition = word_definitions["Pizza"]
apple_definition = word_definitions["Apple"]
# print(f"Pizza: {pizza_definition}, Apple: {apple_definition}")

"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""
for key, value in word_definitions.items():
    print(f"The definition of {key} is {value}")