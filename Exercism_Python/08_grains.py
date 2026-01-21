def square(number):
    if number >= 1 and number <=64:
        return 2**(number-1)
    else:
        raise ValueError("square must be between 1 and 64")

def total():
    result = 0
    num = 1
    while num <= 64:
        result += 2**(num-1)
        num += 1
    return result

num = int(input("add number"))
print(square(num))
