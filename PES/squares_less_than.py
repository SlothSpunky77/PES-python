#Display all squares less than or equal to n
n = int(input("Enter a number: "))
i = 1
while (i*i) <= n:
    print(i*i,end=' ')
    i = i + 1
