username = input("What is your username? ")
is_admin = username == "admin"

password = input("What is your password? ")
is_password_correct = password == "dinosaursYellowChair"

if is_admin and is_password_correct:
    print("Welcome")

if not is_admin or not is_password_correct:
    print("Access denied!")

"""
If statement = used to run a block of code depending on whether a condition is True or False
"""
password = input("password: ")

if password == "jumanji":
    print("Success")

