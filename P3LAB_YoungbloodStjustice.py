# St. Justice Youngblood
# P3LAB
# 6/25/25
# Desc: A program that will convert an inputted dollar/cent amount into the appropriate change.

# Get user input
valueMoney = float(input("Enter the amount of money as a float: $"))

if valueMoney == 0.00:
    print("No change")

# Convert to cents
totalCents = int(valueMoney * 100)

# Get Dollars and print
dollars = totalCents // 100
leftOver = totalCents % 100

if int(valueMoney) == 1:
    print("1 Dollar")
elif int(valueMoney) > 1:
    print(f"{dollars} Dollars")


# Get Quarters and print
quarters = leftOver // 25
remaining = leftOver - (quarters * 25)
if quarters == 1:
    print("1 Quarter")
elif quarters > 1:
    print(f"{quarters} Quarters")

# Get Dimes and print
dimes = remaining // 10
leftOver = leftOver - (dimes * 10)
if dimes == 1:
    print("1 Dime")
elif dimes > 1:
    print(f"{dimes} Dimes")

# Get Nickels  and print
nickels = leftOver // 5
remaining = leftOver - (nickels * 5)
if nickels == 1:
    print("1 Nickel")
elif nickels > 1:
    print(f"{nickels} Nickels")

# Get Pennies and print
pennies = leftOver
if pennies == 1:
    print("1 Penny")
elif pennies > 1:
    print(f"{pennies} Pennies")


