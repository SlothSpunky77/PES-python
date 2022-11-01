n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
i = 1
c1 = 0
c2 = 0
while i <= n1 or i <= n2:
    if n1%i == 0:
        c1 = c1 + 1
    if n2%i == 0:
        c2 = c2 + 1
    i = i + 1
if c1 == 2 or c2 == 2:
    print("The numbers are co-prime.")
else:
    print("The numbers are not co-prime.")
