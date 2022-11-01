import time
import math
print("Part one: Three sides.")
time.sleep(1)
s1 = float(input("Enter the first side: "))
s2 = float(input("Enter the second side: "))
s3 = float(input("Enter the third side: "))
h = (s1+s2+s3)/2
a1 = math.sqrt(h*(h - s1)*(h - s2)*(h - s3))
print("Area of the triangle:",a1)
time.sleep(2)
print("Part two: Two sides and one angle.")
time.sleep(1)
s1 = float(input("Enter the first side: "))
s2 = float(input("Enter the second side: "))
angle = float(input("Enter the angle in radians: "))
a2 = (s1 * s2 * math.sin(angle)) / 2
print("Area of the triangle:",a2)
time.sleep(2)
print("Part three: One side and height.")
time.sleep(1)
s = float(input("Enter the side: "))
h = float(input("Enter the altitude: "))
a = s * h * 0.5
print("The area of the triangle is:",a)
