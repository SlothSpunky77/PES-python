import math
print("Area and perimeter of a triangle:")
s1 = float(input("Enter the first side of the triangle: "))
s2 = float(input("Enter the second side of the triangle: "))
s3 = float(input("Enter the third side of the triangle: "))
print("Perimeter of the triangle:",s1+s2+s3)
h = (s1+s2+s3)/2
a = math.sqrt(h*(h - s1)*(h - s2)*(h - s3))
print("Area of the triangle:",a)
