s = input("Enter a string of four characters: ")
print("Converting the letters to the letter of next ASCII value:")
for i in s:
    if ord(i) == 90 or ord(i) == 122:
        print(i,end = "")
        continue
    print(chr(ord(i)+1),end = "")
print()
