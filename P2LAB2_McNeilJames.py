# James McNeil
# 9/11/2024
# P2LAB2
# Using dictionaries

#Create a dictionary
cars = {"Camaro":18.21, "Prius": 52.36, "Model S":110, "Silverado":26}

# Get all keys
keys = cars.keys()

# Print all keys
print(keys)
print()

# Get input from user and assign to variable
user_car = input("Enter a vehicle to see its mpg: ")
print()
print("The", user_car, "gets", cars[user_car], "mpg.")

# Get miles to drive
miles_to_drive = int(input("How many miles will you drive the " + user_car + "?"))

# Calculate gallons needed
gallons_needed = miles_to_drive/cars[user_car]

print(round(gallons_needed, 2), "gallon(s) of gas are needed to drive the", user_car, miles_to_drive, "miles.")
