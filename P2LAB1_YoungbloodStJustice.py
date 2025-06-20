# St. Justice Youngblood
# 6/19/25
# P2LAB1
# Desc: This program will calculate the diameter, circumference, and area of a circle.

import math 

print("What is the radius of the circle?", end=" ")
radius = float(input())

diameter = 2 * radius

circumference = 2 * math.pi * radius

area = math.pi * radius ** 2

print("\nThe diameter of the circle is", end=" ")
print(f"{diameter:.1f}")

print("\nThe circumference of the circle is", end=" ")
print(f"{circumference:.2f}")

print("\nThe area of the circle is", end=" ")
print(f"{area:.3f}")
