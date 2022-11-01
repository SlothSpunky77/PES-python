print("To display a sequence separated by + and *")
s = 0
p = 1
i = int(input("Enter a number: "))
for c in range(1,i+1):
    if c < i:
        print(c,end="+")
        s = s + c
    else:
        print(c,end="=")
        s = s + c
print(s)
for c in range(1,i+1):
    if c < i:
        print(c,end="*")
        p = p * c
    else:
        print(c,end="=")
        p = p * c
print(p)
