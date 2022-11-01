n = int(input("Enter a number: "))
c = 0
print("The factors are: ")
for i in range(1,n+1):
    if n % i == 0:
        print(i)
        c += 1
if c == 2:
    print("The number is a prime number.")

