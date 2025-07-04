# St. Justice Youngblood
# 7/4/25
# P4HW2
# Desc: This program will calculate overpay and regular pay once the user inputs their name, pay rate, and hours worked.
# As well as allowing them to calculate the total for multiple employees. 

empName = input("Enter employee's name or 'Done' to terminate: ")

# Create a list to hold totals
empEntered = []
empTotal_OT = []
empRegHourTotal = []
empGrossTotal = []

while empName != "Done":
    empHours = float(input(f"How many hours did {empName} work? "))
    empPayRate = float(input(f"What is {empName}'s pay rate? ")) 
    
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

    # Add totals
    
    empEntered.append(empName)
    empTotal_OT.append(overTimePay)
    empRegHourTotal.append(regHourPay)
    empGrossTotal.append(grossPay)

    
    
    # Print values
    print("")
    print(f'{"Employee name:":<5} {empName}')
    print("\nHours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay")
    print(f'{"------------------------------------------------------------------------------------------"}')
    print(f'{empHours:<15} {empPayRate:<11} {overTime:<11} {overTimePay:<15.2f} ${regHourPay:<13.2f} ${grossPay:.2f}')

    # Prompt user to reuse the program or end it
    print("")
    empName = input("Enter employee's name or 'Done' to terminate: ")

# Display total values

sumEmp_OT = sum(empTotal_OT)
sumEmp_RegHour = sum(empRegHourTotal)
sumEmp_Gross = sum(empGrossTotal)

print("")
print(f'Total number of employees entered: {len(empEntered)}')
print(f'Total amount paid for overtime: ${sumEmp_OT:.2f}')
print(f'Total amount paid for regular hours: ${sumEmp_RegHour:.2f}')
print(f'Total amount paid in gross: ${sumEmp_Gross:.2f}')


# - - Pseudocode - -
# Display "Enter employee's name or 'Done' to terminate: "
# Input empName

# Declare Real overTime
# Declare Real overTimePay

# Declare (LIST) empEntered
# Declare (LIST) empTotalOT
# Declare (LIST) empRegHourTotal
# Declare (LIST) empGrossTotal

# While NOT(empName == "Done") Then
#       Display "How many hours did ", {empName}, "work? "
#       Display "What is ", {empName}, "'s pay rate? "
#
#       If empHours > 40 Then
#           Set overTime = empHours - 40
#           Set overTimePay = empPayRate * (overTime * 1.5)
#       Else
#           Set overTime = 0
#           Set overTimePay = 0
#
#       Set regHourPay = empPayRate * (empHours - overTime)
#       Set grossPay = regHourPay + overTimePay
#
#       empEntered = add(empName)
#       empTotal_OT = add(overTimePay)
#       empRegHourPay = add(regHourPay)
#       empGrossTotal = add(grossPay)
#
#       Display "Employee name:", {empName}
#       Display "Hours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay"
#       Display {empHours}, {empPayRate}, {overTime}, {overTimePay}, "$", {regHourPay}, "$", {grossPay}
#
#
# Display ""
# Display "Total number of employees entered: ", len(empEntered) 
# Display "Total amount paid for overtime: $", sum(empTotalOT)
# Display "Total amount paid for regular hours: $", sum(empRegHourTotal)
# Display "Total amount paid in gross: $", sum(empGrossTotal)


