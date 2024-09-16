# Write a program.To check the type of a given character....
character = (input("Enter a character"))
if character.isalpha():
    if character.isupper():
        print(f"{character} is uppercase alphabet")
    else:
        print(f"{character} is lowercase alphabet")
else:
    if character.isnumeric():
        print(f"{character} is number")
    else:
        print(f"{character} is a special character")
        