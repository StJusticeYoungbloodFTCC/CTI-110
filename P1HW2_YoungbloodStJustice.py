# St. Justice Youngblood
# 6/11/25
# P1HW2
# (Travel expense calculator)
# Brief Desc: - {Calculates and displays travel expenses}
# -[This program will prompt the user to enter their budget and travel destination.
# -Along with how much they will spend on gas, food, and accommodations.
# -Lastly, it will add the expenses together, subtract them from the budget, and display the final result.]

# --Variables--
# budgetInt
# location
# fuelInt
# accommodationInt
# foodInt
# --

# - - Get user's  budget and expenses - -
# Display "This program calculates and displays travel expenses."
# Display "Enter Budget: "
# Input budgetInt
print("This program calculates and displays travel expenses\n")
print("Enter budget:", end=" ")
budgetInt = int(input())

# Display "Enter your travel destination: "
# Input location
print("\nEnter your travel destination:", end=" ")
location = input()

# Display "How much do you think you will spend on gas?"
# Input fuelInt
print("\nHow much do you think you will spend on gas?", end=" ")
fuelInt = int(input())

# Display "Approximately, how much will you need for accommodation/hotel?"
# Input accommodationInt
print("\nApproximately, how much will you need for accommodation/hotel?", end=" ")
accommodationInt = int(input())

# Display "Last, how much do you need for food?"
# Input foodInt
print("\nLast, how much do you need for food?", end=" ")
foodInt = int(input())

# Separation header
# Display "------------Travel Expenses------------"
print("\n------------Travel Expenses------------")

# Display the user's inputted info, calculate expenses, subtract from the budget, and display the remaining balance. 
# Display "Location: ", location
print("Location:", location)
# Display "Initial Budget: ", budgetInt
print("Initial Budget:", budgetInt)

# Display "Fuel: ", fuelInt
print("\nFuel:", fuelInt)
# Display "Accommodation: ", accommodationInt
print("Accommodation:", accommodationInt)
# Display "Food: " foodInt
print("Food:", foodInt)

# --Calculations--

# Set expensesInt = fuelInt + accomodationInt + foodInt
expensesInt = fuelInt + accommodationInt + foodInt
# Set budgetInt = budgetInt - expensesInt
budgetInt = budgetInt - expensesInt

# Display "Remaining Balance: ", budgetInt
print("\nRemaining Balance:", budgetInt)



