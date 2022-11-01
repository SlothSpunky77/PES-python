import math
a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))
if a+b>=c and b+c>=a and a+c>=b:
    print("The triangle is valid.")
    h = (a+b+c)/2
    area = math.sqrt(h*(h - a)*(h - b)*(h - c))
    print("Area of triangle:",area)
else:
    print("Invalid triangle.")
