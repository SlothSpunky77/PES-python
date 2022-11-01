n = int(input("Enter the number of rows:"))
c = 0
for a in range(n,0,-1):
    l = 65+c
    i = 0
    while i in range(a):
        print(chr(l),end='')
        l = l + 1
        i = i + 1
    c = c + 1
    print()
