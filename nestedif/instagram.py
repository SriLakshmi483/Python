credentials = {"lakshmi":"@483","pranu":"@567","nihi":"@468","rakesh":"@476"}
username = input("Enter username")
password = input("Enter password")
if username in credentials:
    if password == credentials[username]:
        print("Logged Succesfully")
    else:
        print("Incorrect Password")
else:
    print("Username does not exists")