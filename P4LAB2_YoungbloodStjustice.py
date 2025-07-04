# St. Justice Youngblood
# 7/3/25
# P4LAB2
# Desc: A program that will calculate a positive integer * (1-12). 

# Create a start and stop for the while loop.
programRun = "yes"
# Variable for the counter
counter = 1

# Get user's integer, if it is any number below zero, the user will be prompted to run the program again.
# If it's a positive integer, the user will be displayed the result of their integer * 1-12. 
while programRun == "yes":
    userInt = int(input("Enter an integer: "))
    print("")
    if userInt < 0:
        print("This program does not handle negative numbers.")
    else:
        for oneTwelve in range(12):
            print(f"{userInt} * {counter} = {userInt * counter}")
            counter += 1
            oneTwelve += 1
    print("")
    programRun = input("Would you like to run the program again? Enter (yes/no): ")
    print("")
    counter = 1
print("Exiting program...")

