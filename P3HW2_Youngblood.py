# St. Justice Youngblood
# 6/26/2025
# P3HW2
# Desc: This program will calculate a user's overtime hours,
# overtime pay, regular hour pay, and gross pay
# after they input their name, hours worked, and hourly pay rate.  


# Get user input for naame, hours worked, and pay rate
empName = input("Enter employee's name: ")
empHours = float(input("Enter number of hours worked: "))
empPayRate = float(input("Enter employee's pay rate: "))

# Calculate for overtime
if empHours > 40:
    overTime = float(empHours - 40)
    overTimePay = float(empPayRate * (overTime * 1.5))
else:
    overTime = float(0)
    overTimePay = float(0)
# Calculate Regular hour pay and Gross pay
regHourPay = empPayRate * (empHours - overTime)
grossPay = regHourPay + overTimePay

print("-------------------------------------")
print(f'{"Employee name:":<5} {empName}')
print("\nHours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay")
print(f'{"------------------------------------------------------------------------------------------"}')
print(f'{empHours:<15} {empPayRate:<11} {overTime:<11} {overTimePay:<15.2f} ${regHourPay:<13.2f} ${grossPay:.2f}')
