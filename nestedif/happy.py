# Write a program to consider an integer number. Print happy if the number is divisible by two. Print SAD if the number is divisible by 5 and print square of the numbers only if it is divisible by seven else print the number as it is............................
num = int(input("Enter a integer num:"))
if num%7 == 0:
    print(num**2)
elif num%2 == 0:
    print("Happy")
elif num%5 == 0:
    print("Sad")
else:
    print(num)