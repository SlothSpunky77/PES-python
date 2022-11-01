s1 = float(input("Enter the first side: "))
s2 = float(input("Enter the second side: "))
s3 = float(input("Enter the third side: "))
s4 = float(input("Enter the fourth side: "))
d1 = float(input("Enter the first diagonal: "))
d2 = float(input("Enter the second diagonal: "))
if s1 == s2 == s3 == s4 and d1 == d2:
    print("The shape is a square.")
elif s1 == s2 == s3 == s4 and d1 != d2:
    print("The shape is a rhombus.")
elif s1 == s3 and s2 == s4 and d1 != d2:
    print("The shape is a parallelogram.")
elif s1 == s3 and s2 == s4 and d1 == d2:
    print("The shape is a rectangle.")
