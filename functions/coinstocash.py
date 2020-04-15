def calc_dollars(**coins):
    coins = coins.items()
    print(coins)

    # The function should look at each key (pennies, nickels, dimes and quarters) and perform the appropriate math on the integer value to determine how much money you have in dollars. Store that value in a variable named `dollarAmount` and print it.
    for key, value in coins:
        if key == "pennies":
            print(f"{key}: {value}")
        elif key == "nickels":
            print(f"{key}: {value}")
        elif key == "dimes":
            print(f"{key}: {value}")
        elif key == "quarters":
            print(f"{key}: {value}")

calc_dollars(pennies= 342, nickels=9, dimes=32, quarters=4)