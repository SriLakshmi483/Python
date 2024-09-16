#Program to print middle value of the given heterogeneous tuple collection only if the middle value is string and having the length greater than 3.................
tuple1 = eval(input("Enter a collection:"))
if len(tuple1) > 3:
    string1 = tuple1[len(tuple1) // 2]
    if type(string1) is str :
        print(f"{string1} is a string")
    else:
        print(f"{string1} is not a string")
else:
    print(f"{tuple1} length has less than 3")