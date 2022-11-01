print("X-axis:")
x1 = float(input("Enter for x1: "))
x2 = float(input("Enter for x2: "))
x3 = float(input("Enter for x3: "))
print("Y-axis")
y1 = float(input("Enter for y1: "))
y2 = float(input("Enter for y2: "))
y3 = float(input("Enter for y3: "))
a = (x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))/2
if a == 0:
    print("A triangle cannot be formed.")
else:
    cx = (x1+x2+x3)/3
    cy = (y1+y2+y3)/3
    print("The coordinates of the centroid are: (",cx,",",cy,")")
