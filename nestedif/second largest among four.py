num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))
num4 = int(input("Enter num4: "))
if num1 > num2 and num1 > num3 and num1 > num4:
    if num2 > num3 and num2 > num4:
        if num3 > num4:
            print(f"{num2} is second largest")
        else:
            print(f"{num3} is second largest")
    else:
        print(f"{num4} is second largest")
elif num2 > num3 and num2 > num4 and num2 > num1:
    if num3 > num1 and num3 > num4:
        if num4 > num1:
            print(f"{num3} is second largest")
        else:
            print(f"{num4} is second largest")
    else:
        print(f"{num1} is second largest")
elif num3 > num2 and num3 > num1 and num3 > num4:
    if num4 > num1 and num4 > num2:
        if num1 > num2:
            print(f"{num4} is second largest")
        else:
            print(f"{num1} is second largest")
    else:
        print(f"{num2} is second largest")
else:
    if num1 > num2 and num1 > num3:
        if num2 > num3:
            print(f"{num1} is second largest")
        else:
            print(f"{num2} is second largest")
    else:
        print(f"{num3} is second largest")
        
# ..................One more method......................... 
       
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))
num4 = int(input("Enter num4: "))
if num1 > num2 and num1 > num3 and num1 > num4:
    if num2 > num3 and num2 > num4:
        print(f"{num2} is second largest")
    elif num3 > num4:
        print(f"{num3} is second largest")
    else:
        print(f"{num4} is second largest")
elif num2 > num3 and num2 > num4 and num2 > num1:
    if num3 > num1 and num3 > num4:
        print(f"{num3} is second largest")
    elif num4 > num1:
        print(f"{num4} is second largest")
    else:
        print(f"{num1} is second largest")
elif num3 > num2 and num3 > num1 and num3 > num4:
    if num4 > num1 and num4 > num2:
        print(f"{num4} is second largest")
    elif num1 > num2:
        print(f"{num1} is second largest")
    else:
        print(f"{num2} is second largest")
else:
    if num1 > num2 and num1 > num3:
        print(f"{num1} is second largest")
    elif num2 > num3:
        print(f"{num2} is second largest")
    else:
        print(f"{num3} is second largest")