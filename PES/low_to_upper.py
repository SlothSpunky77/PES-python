print("To convert from lowercase to uppercase along with it's ASCII code.")
w = input("Enter a four letter word in lowercase: ")
W = ""
for i in w:
    if i.isupper() == True:
        print("Invalid.")
        exit()
for i in w:
    W = W + i.upper()
    print(ord(i.upper()))
print(W)
