class Pizza:
    def __init__(self):
        self.size = "Medium"
        self.crust_type = "Regular"
        self.toppings = ["Pepperoni"]

    def add_topping(self, topping):
        self.toppings.append(topping)

    # Could make this more dynamic to include as many toppings are added, but not sure how to do that exactly.
    def print_order(self):
            print(f"I would like a {self.size} pizza with {self.toppings[0]} and {self.toppings[1]}")

tylers_pizza = Pizza()

tylers_pizza.add_topping("Pineapple")

tylers_pizza.print_order()