# James McNeil
# 9/23/24
# P4HW1
# Use a loop to add valid grades to a list


# Create an empty lidt
grade_list = []

# Get the number of scores that users want to enter
num_scores = int(input("How many scores do you want to enter? "))

# For loop to get the values ofthe scores
for score in range(num_scores):
    num_grade = int(input(f"Enter score #{score+1}: "))

    # If the grade is INVALID, go into while loop
    while num_grade < 0 or num_grade > 100:
        print("INVALID grade entered!!!\n")
        print("Score should be between 0 and 100\n")
        num_grade = int(input(f"Enter score #{score+1} again: "))
    # While loop breaks, grade is valid, add it to list
    grade_list.append(num_grade)

# All loops broken
print(f"The valid grades are: {grade_list}")

print(f"The lowest grade is: {min(grade_list)}")

# Remove lowest grade from list
grade_list.remove(min(grade_list))

print(f"The final grades are: {grade_list}")
