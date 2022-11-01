r = int(input("Enter the number of rows: "))
for i in range(r+1):
    c = 1
    while c <= i:
        print(c,end='')
        c = c + 1
    if i != 1:
        c = i-1
        while c > 0:
            print(c,end='')
            c = c - 1
    print()
