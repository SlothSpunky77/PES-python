import cmath
a = int(input("Enter the value for coefficient a: "))
b = int(input("Enter the value for coefficient b: "))
c = int(input("Enter the value for coefficient c: "))
d = (b ** 2) - (4 * a * c)
r1 = (-b + cmath.sqrt(d))/(2 * a)
r2 = (-b - cmath.sqrt(d))/(2 * a)
print("The roots are:",r1,"and",r2)
