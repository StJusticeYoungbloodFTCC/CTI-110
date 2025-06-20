# St. Justice Youngblood
# 6/19/25
# P2LAB2
# Desc: This program will allow the user to see
# the mpg on a car within the dictionary. It will then calculate 
# the needed gallons of gas required after the user inserts how many
# miles they wish to go on the car.

my_dict = {
  # Automobile - MPG #
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26,
}

# Display's the available cars
keys = my_dict.keys()
print(keys)

# Get the user's perfered automobile
print("\nEnter a vehicle to see it's mpg:", end=" ")
userCar = input()
carMPG = my_dict[userCar]

# Display mpg
print("\nThe", userCar, "gets", my_dict[userCar], "mpg.\n")

# Prompt the user to see how many miles they will drive 
print(f"How many miles will you drive the {userCar}?", end=" ")
userMiles = float(input())

# Calculate the gallons of gas the user will need for their entered miles
userGallons = userMiles / carMPG

# Display the needed gallons of gas for the user's entered miles
print(f"\n{userGallons:.2} gallon(s) of gas are needed to drive the {userCar} {userMiles} miles.\n")

