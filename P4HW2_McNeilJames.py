# James McNeil
# 9/25/24
# P4HW2
# Calculate pay rates using if/else statements
#Get info from user

# Create variables for num employees and their pay
num_emp = 0
total_ot = 0
total_reg = 0
total_gross = 0

name = input("Enter employee's name: ")

while name != "Done":
    # Add one to the number of employees
    num_emp += 1
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
        gross_pay = reg_pay_amt + ot_pay_amt
    else:
     
        reg_pay_amt = hours * pay_rate
         
        ot_hours = 0
         
        ot_pay_amt = 0
        # Calculate gross pay
        gross_pay = reg_pay_amt + ot_pay_amt

    #Add to employee pay
    total_ot += ot_hours
    total_reg += reg_pay_amt
    total_gross += gross_pay
    print()
    #Display headings
    print(f"{'Hours Worked':<15}{'Pay Rate':<10}{'Overtime Hours':<18}{'Overtime Pay':<15} {'Regular Pay':<15} {'Gross Pay':<15}")
    print("-" * 100)
    print(f"{hours:<15}${pay_rate:<15.2f} {ot_hours:<15}${ot_pay_amt:<15.2f}${reg_pay_amt:<15.2f}${gross_pay:<15.2f}")

    # Get new input for the name variable - stop endless loop
    name = input("Enter employee's name: ")
        

# Loop ends here
print("Goodbye")

# Print total paid and num employees
print(f"Total numbers of employees entered : {num_emp}")
print(f"Total amount paid for overtime: ${total_reg:.2f}")
print(f"Total amount paid for gross pay: ${total_gross:.2f}")
