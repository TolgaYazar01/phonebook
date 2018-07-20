students = {'nicole': ['dog', '222-213-1029', 'math', '1390'], 'ken': ['cat', '207-983-2717', 'art', 'pin' '9364']}

username = input("Please enter username: ")
while not students.get(username):
    print("Invalid Username")
    username = input("Please enter username: ")


password = input("Please enter password: ")
actual_password = students[username][0]
while password != actual_password:
    print("Incorect Password. Please try again!")
    password = input("Please retry password: ")
if(password == actual_password):
    print("Welcome to your Account")
else:
    print("Access Denied")

pin = input("Please enter Pin code: ")
    
