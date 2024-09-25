# James McNeil
# 9/25/24
# P4LAB2
# Using a while loop with a for loop

# Create a loop that runs until the user enters "no"


run_again = ""

while run_again != "no":
    user_num = int(input("Enter an integer: "))
    print()
    if user_num < 0:
        print("This program does not handle negative numbers!!")
    else:
        for num in range(12):
            print(f"{user_num} * {num+1} = {user_num * (num+1)}")
            print()

            
    run_again = input("\nWould you like to run the program again? ")
    print()


# Loop ends
print("\nGoodbye\n")
