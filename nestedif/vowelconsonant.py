char = input("Enter character:")
list1 = []
if char.isalpha():
    if char in "aeiouAEIOU":
        list1.append(char)
        print(list1)
    else:
        print(ord(char))
else:
    print("It is not a alphabet")
    
  