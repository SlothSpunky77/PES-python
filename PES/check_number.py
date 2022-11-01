#check whether a given number is a perfect square, fibonacci number or a perfect power of 2
n = int(input("Enter a number: "))
i = 1
while i <= (n // 2):
    if i * i == n:
        print("It is a perfect square of",i)
    i = i + 1

a = 1
b = 1
c = 0
print("Fibonacci series:")
while c < n:
    c = a + b
    print(c,end = '  ')
    if c == n:
        print()
        print("It is part of the Fibonacci series.")
    a = b
    b = c

c = 1
while c <= (n/2):
    if (2 ** c) == n:
        print()
        print("It is a perfect power of 2.")
    c = c + 1

