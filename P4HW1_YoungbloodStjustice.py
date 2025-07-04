# St. Justice Youngblood
# 7/3/25
# P4HW1
# Desc: This program will calculate a user's grade values and will display the grade letter
# and average after dropping the lowest grade. 

# -- Get the user's grade values, check for negative values. --
counter = 1

score_Amount = int(input("How many scores do you want to enter? "))
print("")

# -- Create a list to store user's inputted grades --
gradesModule = []

for i in range(score_Amount):
    inputHold = float(input(f"Enter score #{counter}: "))
    if inputHold < 0 or inputHold > 100:
        print("")
        print("INVALID Score entered!")
        print("Score should be between 0 and 100")
        inputHold = float(input(f"Enter score #{counter} again: "))
    gradesModule.append(float(inputHold))
    counter += 1

# -- Calculate score average and letter grade --



print("\n-----------------Results-----------------")

print(f'{"Lowest Grade":<15}: {min(gradesModule)}')

gradesModule.remove(min(gradesModule))
print(f'{"Modified List":<15}: {(gradesModule)}')

average = sum(gradesModule) / len(gradesModule)
print(f'{"Scores Average":<15}: {average:.2f}')

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print(f'{"Grade":<15}: {(grade)}')

print("---------------------------------------------")



# Pseudocode mockup

# -- Get the user's grade values, check for negative values. --
# Declare Integer counter = 1
# Declare Integer score_amount

# Display "How many scores do you want to enter? "
# Input score_Amount

# -- Create a list to store user's inputted grades --

# For i = 1 To score_amount Step 1
#       Display "Enter score #", counter, ": "
#       Input inputHold
#       If inputHold < 0 OR inputHold > 100 Then
#           Display "INVALID Score entered!"
#           Display "Score should be between 0 and 100"
#           Display "Enter score #", counter, "again: "
#           Input inputHold
#       -- (Add inputHold to list) --
#       End If
# End For

# -- Calculate score average and letter grade --

# Display "------------------Results--------------------"

# Display "Lowest Grade : ", Lowest of gradesModule)

# -- (Remove lowest value from gradesModule) --
# Display "Modified list : ", gradesModule

# Declare Real average = sum of (gradesModule) / length of (gradesModule)
# Display "Scores Average : ", average

# Declare grade = "N"

# If average >= 90 Then 
#       Set grade = "A"
# Else If average >= 80 Then
#       Set grade = "B"
# Else If average >= 70 Then
#       Set grade = "C"
# Else If average >= 60 Then
#       Set grade = "D"
# Else
#   Set grade = "F"
# End If

# Display "Grade: ", grade

# Display "------------------------------------------------------"


