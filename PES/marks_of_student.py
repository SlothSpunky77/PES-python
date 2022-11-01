print("To find the percentage of marks of five subjects.")
i = 1
s = 0
print("The marks should be out of 100.")
while i <= 5:
    print("Enter the marks of subject",i,":")
    m = float(input())
    s = s + m
    i = i + 1
print("The percentage is:",s/5)
