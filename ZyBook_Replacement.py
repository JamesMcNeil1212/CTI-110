# James McNeil
# 10/2/24
# zyBooks Function Replacement Assignment
 


def is_even(num):
    remainder = num % 2

    
    if remainder == 0:
        return True
    else:
        return False


def find_maximum(a, b, c):
    myList = [a,b,c]
    maximum = max(myList)

    return maximum


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32


    return fahrenheit


def main():
    even = is_even(7)
    print(f"The number is even, {even}")


    print(f"The maximum is {find_maximum(3,6,9)}")
    

    print(f"The temperature in fahrenheit is {celsius_to_fahrenheit(30)}")

    
if __name__ == "__main__":
    main()
