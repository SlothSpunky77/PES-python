i = 1
s = 0
while i <= 12:
    print("Month",i,":")
    n = int(input("Enter the number of cameras sold: "))
    if n == 0:
        i = i + 1
        continue
    price = int(input("Enter the price of each camera: "))
    commission = (n*price*12)/100
    bonus = 200*n
    s = s + bonus + commission
    i = i + 1
s = s + 25000
print("The salary of the cameraman is: ",s)
