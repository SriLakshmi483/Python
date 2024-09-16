num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))
num3 = int(input("Enter num3:"))
num4 = int(input("Enter num4:"))
if num1 > num2:
    if num1 > num3:
        if num1 > num4:
            print(f"{num1} is greater")
elif num2 > num3:
    if num2 > num4:
        print(f"{num2} is greater")
elif num3 > num4:
    print(f"{num4} is greater")
else:
    print(f"{num4} is greater")
    