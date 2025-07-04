# St. Justice Youngblood
# 6/26/2025
# P3HW1
# CTI-110
# Desc: This program takes a number grade, determines the average, and displays the letter grade for the average.

# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine the lowest, highest, sum, and average for grades

low = min(grades)
high = max(grades)
sum = sum(grades)
avg = sum / len(grades)

# Determine the letter grade for the average

print("\n------------Results------------")
print(f'{"Lowest Grade:":<20} {low}')
print(f'{"Highest Grade:":<20} {high}')
print(f'{"Sum of Grades:":<20} {sum}')
print(f'{"Average:":<20} {avg:.2f}')
print("--------------------------------------")

if avg >= 90:
    print('Your grade is: A')
elif avg > 80:
    print('Your grade is: B')
elif avg > 70:
    print('Your grade is: C')
elif avg > 60: 
    print('Your grade is D')
else:
    print('Your grade is: F') 




