def calc_dollars(**coins):
    coins = coins.items()

    total = 0

    # The function should look at each key (pennies, nickels, dimes and quarters) and perform the appropriate math on the integer value to determine how much money you have in dollars. Store that value in a variable named `dollarAmount` and print it.
    for key, value in coins:
        if key == "pennies":
            dollar_amt = value / 100
            total += dollar_amt
        elif key == "nickels":
            dollar_amt = value / 20
            total += dollar_amt
        elif key == "dimes":
            dollar_amt = value / 10
            total += dollar_amt
        elif key == "quarters":
            dollar_amt = value / 4
            total += dollar_amt

    print(total)

calc_dollars(pennies= 342, nickels=9, dimes=32, quarters=4)