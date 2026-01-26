def is_armstrong_number(number):
    total = 0 

    for n in str(number):
        total += int(n)**len(str(number))
    return total == number