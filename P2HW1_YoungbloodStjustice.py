# St. Justice Youngblood
# 6/19/25
# P2HW1
# This program will calculate and display travel expenses

# - - Get user's  budget and expenses - -
# Display "This program calculates and displays travel expenses."
# Display "Enter Budget: "
# Input budgetFlt
print("This program calculates and displays travel expenses\n")
print("Enter budget:", end=" ")
budgetFlt = float(input())

# Display "Enter your travel destination: "
# Input location
print("\nEnter your travel destination:", end=" ")
location = input(str())

# Display "How much do you think you will spend on gas?"
# Input fuelFlt
print("\nHow much do you think you will spend on gas?", end=" ")
fuelFlt = float(input())

# Display "Approximately, how much will you need for accommodation/hotel?"
# Input accommodationFlt
print("\nApproximately, how much will you need for accomodation/hotel?", end=" ")
accommodationFlt = float(input())

# Display "Last, how much do you need for food?"
# Input foodFlt
print("\nLast, how much do you need for food?", end=" ")
foodFlt = float(input())

# Separation header

# Display "------------Travel Expenses------------"
print("\n------------Travel Expenses------------")

# Display "Location: ", location
print(f'{"Location:":<20} {location}')
# Display "Initial Budget: ", budgetFlt
print(f'{"Initial Budget:":<20} ${budgetFlt:.2f}')
# Display "Fuel: ", fuelFlt
print(f'{"Fuel:":<20} ${fuelFlt:.2f}')
# Display "Accommodation: ", accommodationFlt
print(f'{"Accommodation:":<20} ${accommodationFlt:.2f}')
# Display "Food: " foodFlt
print(f'{"Food:":<20} ${foodFlt:.2f}')

print("-----------------------------------------")
 
# --Calculations--

# Set expensesInt = fuelInt + accomodationInt + foodInt
expensesFlt = fuelFlt + accommodationFlt + foodFlt
# Set budgetInt = budgetInt - expensesInt
budgetFlt = budgetFlt - expensesFlt

# Display "Remaining Balance: ", budgetInt
print(f'\n{"Remaining Balance:":<20} ${budgetFlt:.2f}')
