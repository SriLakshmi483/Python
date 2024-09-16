# Program to consider an input string. Print the string as it is if it is palindrome. Print the reverse string if it has an even number of characters. Print all the characters present at an odd index if the string is having an odd number of characters..........
string1 = input("Enter string:")
string2 = string1[::-1]
if string1 == string2:
    print(f"{string1} is a palindrome")
elif len(string2) % 2 == 0:
    print(f"{string2} is a reverse string")
else:
    print(f"{string1[1::2]}")
    