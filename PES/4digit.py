n = int(input("Enter a four digit number: "))
n1 = n // 1000
print(n1)
n2 = (n - (n1*1000)) // 100
print(n2)
n3 = ((n%1000) - (n2*100)) // 10
print(n3)
n4 = (((n%1000) - (n2*100)) - (n3*10)) 
print(n4)
s = n1 + n2 + n3 + n4
print("The sum of digits is:",s)
