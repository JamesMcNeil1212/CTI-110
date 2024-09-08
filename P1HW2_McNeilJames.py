# James McNeil
# 9/7/24
# P1HW2
# Budgeting Traveling Expenses
print("This program calculates and displays travel expenses")
print()
budget=int(input("Enter Budget: "))
print()
travel_destination=input("Enter your travel destination: ")
print()
gas_money=int(input("How much do you think you'll spend on gas? "))
print()
living_fee=int(input("Approximately, how much will you need for accommodation/hotel? "))
print()
food=int(input("Last, how much do you need for food? "))
print()
print("------------Travel Expenses------------")
print("location:", travel_destination)
print("Initial Budget: ", budget)
print()
print("Fuel: ", gas_money)
print("accomodation: ", living_fee)
print("Food: ", food)
print()
leftover_balance= budget-gas_money-living_fee-food
print("Remaining Balance: ",leftover_balance )