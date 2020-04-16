dollarAmount = 8.69

piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}

piggyBank_items = piggyBank.items()

# Your magic Python code here

# I believe I need % to find as many coins will go into the doll amt, 
# but not sure how to apply it. Will circle back later.
def cashToCoins(items):

    for key, value in items:
        print(f"{key}: {value}")

        if key == "quarters":
            value = dollarAmount / 4

            print(f"{key}, {value}")

cashToCoins(piggyBank_items)