# Write a program to find the smallest among three numbers.
num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))
num3 = int(input("Enter num2:"))
if num1 < num2:
    if num1 < num3:
        print(f"{num1} is smaller")
    else:
        print(f"{num3} is smaller")
else:
    if num2 < num3:
        print(f"{num2} is smaller")
    else:
        print(f"{num3} is smaller")