# James McNeil
# 9/18/24
# P3HW2
# Calculate pay rates using if/else statements

#Get info from user
name = input("Enter employee's name: ")
hours = int(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Display name

print("---------------------------\nEmployee name: ", name)

# Determine employee pay
if hours > 40:
    #They have some overtime
    reg_pay_amt = 40 * pay_rate
    ot_pay_rate = 1.5 * pay_rate
    ot_hours = hours - 40
    ot_pay_amt = ot_hours * ot_pay_rate
else:
    reg_pay_amt = hours * pay_rate
    ot_hours = 0
    ot_pay_amt = 0


# Calculate gross pay
gross_pay = reg_pay_amt + ot_pay_amt

print()

#Display headings
print(f"{'Hours Worked':<15}{'Pay Rate':<10}{'Overtime Hours':<18}{'Overtime Pay':<15} {'Regular Pay':<15} {'Gross Pay':<15}")
print("-" * 100)
print(f"{hours:<15}${pay_rate:<15.2f} {ot_hours:<15}${ot_pay_amt:<15.2f}${reg_pay_amt:<15.2f}${gross_pay:<15.2f}")
