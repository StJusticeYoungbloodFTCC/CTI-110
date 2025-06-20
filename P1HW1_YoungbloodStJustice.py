# St. Justice Youngblood
# 6/11/25 
# P1HW1
# Desc: 
# (Exponents: This program will ask the user for any base value,
# -then their exponent, and displays the solved equation.)
# 
# (Add and Sub: The second part of this program will ask for a
# -starting integer, an integer to add to it, and an integer to
# -subtract from it. It will then display the solved equation.) 

# --- Header for Exponents ---
print("-----Calculating Exponents----\n\n")

# -- Calculations
print("Enter an integer as the base value:", end=" ")
baseInt = int(input()) 
print("Enter an integer as the exponent:", end=" ")
expoInt = int(input())
sumExpo = baseInt ** expoInt

# - Final statement -
print("\n\n", baseInt, "raised to the power of", expoInt, "is", sumExpo, "!!")

# --- Header for Add and Sub ---
print("\n\n-----Addition and Subtraction----\n\n")

# -- Calculations, () in fullSum added for clarity. 
print("Enter a starting integer:", end=" ")
startInt = int(input())
print("Enter an inte1ger to add:", end=" ")
addInt = int(input())
print("Enter an integer to subtract:", end=" ")
subInt = int(input())
fullSum = (startInt + addInt) - subInt
 
# - Final statement -
print("\n\n", startInt, "+", addInt, "-", subInt, "is equal to", fullSum)
