print("Program to display all integers within the range 100 to 200 whose sum of digits is an even number.")

for i in range(100,201):
    d1 = (i // 100)
    d2 = (i % 100) // 10
    d3 = (i % 100) % 10
    if (d1+d2+d3)%2 == 0:
        print(i)

