# St. Justice Youngblood
# 7/10/25
# P5LAB
# Desc: A self-checkout simulation that will ask the user how much money they will put
# into a self-checkout machine, and it will generate the change they will receive back. 

import random

def disperce_change(changeOwed):
    
    changeRem = round(changeOwed * 100)

    # Get Dollars and print
    dollars = changeRem // 100
    changeRem = changeRem % 100

    if dollars == 1:
        print("1 Dollar")
    elif dollars > 1:
        print(f"{dollars} Dollars")


    # Get Quarters and print
    quarters = changeRem // 25
    changeRem = changeRem - (quarters * 25)
    if quarters == 1:
        print("1 Quarter")
    elif quarters > 1:
        print(f"{quarters} Quarters")

    # Get Dimes and print
    dimes = changeRem // 10
    changeRem = changeRem - (dimes * 10)
    if dimes == 1:
        print("1 Dime")
    elif dimes > 1:
        print(f"{dimes} Dimes")

    # Get Nickels  and print
    nickels = changeRem // 5
    changeRem = changeRem - (nickels * 5)
    if nickels == 1:
        print("1 Nickel")
    elif nickels > 1:
        print(f"{nickels} Nickels")

    # Get Pennies and print

    if changeRem == 1:
        print("1 Penny")
    elif changeRem > 1:
        print(f"{changeRem} Pennies")

def main(): 
    userOwe = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${userOwe}")

    valueMoney = float(input("How much cash will you put in the self-checkout? "))
    changeOwed = valueMoney - userOwe
    print(f"Change is: ${changeOwed:.2f}")
    print()

    disperce_change(float(changeOwed))

# Call main

main()