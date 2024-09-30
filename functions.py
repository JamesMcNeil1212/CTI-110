# User-defined functions

# Define the add function

import random

def add(x,y):
    """This function adds two integers, x and y"""
    result = x + y
    return result

# Define a non-value returning function
def getList():
    """Create and return a list"""
    myList = []
    for item in range(3):
        myList.append(input("Enter a color: "))
    print(myList)

def getTotal(priceList):
    """Return the sum of a list of numbers"""
    return sum(priceList)



# Create the main fnction
def main():
    # Main program goes here
    rand1 = random.randint(1,100)
    rand2 = random.randint(1,100)

    # Call the add function
    num_sum = add(rand1,rand2)
    print(f"The sum of {rand1} and {rand2} is {num_sum}\n\n")


    # Call the getList function
    getList()

    # Create a list of floats
    myNums = []
    for item in range(4):
        myNums.append(float(input("Enter a price: ")))

    # Call the getTotal function, passing in myNums (List)
    total = getTotal(myNums)
     
     # Print each item in myNums
    print("The values are : ")
    for num in myNums:
        print(num)

    # Print the total
    print(f"The total is ${total:.2f}")


if __name__ == "__main__":
    main()
