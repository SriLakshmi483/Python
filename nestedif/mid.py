# Write a program to print middle Character.Given string only if it is upper case character...................................
word = input("Enter word:")
character = len(word) //2
if word.isupper():
    print(word[character])
else:
    print("Not an uppercase letters")