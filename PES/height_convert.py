import time
print("Convert your height from feet and inches to centimetres.")
f = int(input("Enter the value of feet: "))
i = float(input("Enter the value of inches: "))
cm1 = f * 12 * 2.54
cm2 = i * 2.54
print("Your height is:",cm1+cm2)
time.sleep(1)
print("The other way around:")
c = float(input("Enter your height in centimetres: "))
f_ = int((c / 2.54) / 12)
i_ = (((c / 2.54) / 12) - f) * 12
print("Feet:",f_)
print("Inches:",i_)

