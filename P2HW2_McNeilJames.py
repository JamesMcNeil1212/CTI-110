# James McNeil
# 9/16/24
#P2HW2
# Making a list of grades


Module1 = float(input("Enter grade for Module 1: "))
Module2 = float(input("Enter grade for Module 2: "))
Module3 = float(input("Enter grade for Module 3: "))
Module4 = float(input("Enter grade for Module 4: "))
Module5 = float(input("Enter grade for Module 5: "))
Module6 = float(input("Enter grade for Module 6: "))


grades = []

grades.append(Module1)
grades.append(Module2)
grades.append(Module3)
grades.append(Module4)
grades.append(Module5)
grades.append(Module6)


print()

print("------------Results------------")


Lowest = print(f'{"Lowest Grade: ":<20}', min(grades))
Highest = print(f'{"Highest Grade: ":<20}', max(grades))
Sum = print(f'{"Sum of Grades: ":<20}', sum(grades))
Ave = print(f'{"Average: ":<20}', f"{sum(grades)/len(grades):.2f}")


