# James McNeil
# 9/11/2024
# P2LAB1
# Calculate math related to a circle

# Import the math library
import math

# Get float input from user (radius)
radius = float(input("What is the radius of the circle? "))
print()

#Calculate diameter
diameter = radius *2
print("The diameter of the circle is", diameter)
print()

# Calculate circumference
circum = 2 * math.pi * radius
print("The circumfrence of the circle is", round(circum, 2))

# Calculate the area
area = math.pi * (radius ** 2)
print()
print("The area of the circle is", round(area, 3))
