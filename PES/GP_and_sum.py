print("To print a G.P.: ")
s = 0
a = int(input("Enter the value of a: "))
r = int(input("Enter the value of r: "))
max = int(input("Enter the maximum value: "))
print("G.P.: ")
for i in range(1,max+1):
    t = a*(r**(i - 1))
    print(t)
    s = s + t
print("The sum is:",s)
