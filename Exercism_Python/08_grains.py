def square(number):
    if number >= 1 and number <=64:
        return 2**(number-1)
    else:
        raise ValueError("square must be between 1 and 64")

def total(square):
    counter = 1
    while square <= 64:
        counter += 1

num = int(input("add number"))
print(square(num))