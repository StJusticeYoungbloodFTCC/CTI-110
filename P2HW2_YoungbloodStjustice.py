# St. Justice Youngblood
# 6/20/25
# P2HW2
# This program will ask the user to enter their grades for:
# Module 1-6 tests, then it will display their highest/lowest grade,
# sum of grades, and lastly their grade average from the tests.

# -- Get the user's grade vaules --
# Declare Real module_1
# Display "Enter grade for Module 1: "
# Input module_1
# Repeat for 2-6

module_1 = float(input("Enter grade for Module 1: "))
module_2 = float(input("Enter grade for Module 2: "))
module_3 = float(input("Enter grade for Module 3: "))
module_4 = float(input("Enter grade for Module 4: "))
module_5 = float(input("Enter grade for Module 5: "))
module_6 = float(input("Enter grade for Module 6: "))

# -- Create a list that will organize the recieved values. --
# moduleGrades = [module_1, module_2, module_3, module_4, module_5, module_6]

moduleGrades = [
    module_1,
    module_2,
    module_3,
    module_4,
    module_5,
    module_6
]

# -- Calculate the average of inputed grades --
# Declare Real average
# average = total sum of(moduleGrades) / lenght of(moduleGrades)

average = sum(moduleGrades) / len(moduleGrades)

# -- Display the lowest, highest, sum, and average of grades. --
# Add :<20 at the end of string to organize.

# Display "Lowest Grade: ", min(moduleGrades)
# Display "Highest Grade: ", max(moduleGrades)
# Display "Sum of Grades: ", sum(moduleGrades)
# Display "Average: ", {average:.2f}

print("\n------------Results------------")
print(f'{"Lowest Grade:":<20} {min(moduleGrades)}')
print(f'{"Highest Grade:":<20} {max(moduleGrades)}')
print(f'{"Sum of Grades:":<20} {sum(moduleGrades)}')
print(f'{"Average:":<20} {average:.2f}')
print("--------------------------------------")

