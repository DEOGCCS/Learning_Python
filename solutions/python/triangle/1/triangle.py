def equilateral(sides):
   if sides[0] > 0 and sides[1] > 0 and sides[2] > 0:
        return sides[0] == sides[1] == sides[2]   
   else: 
        return False

def isosceles(sides):
    a, b, c = sides
    a, b, c > 0
    if a+b>c and b+c>a and a+c>b:
        return a == b or b == c or a == c
    else:
        return False

def scalene(sides):
    a, b, c = sides
    a, b, c > 0
    if a+b>c and b+c>a and a+c>b:
        return a != b and b != c and a != c
    else:
        return False