#in this part of this program, it welcomes the name provided to it by the user and checks that the input is not empty.

A = input("Please enter your first name: ")
B = input("Please enter your last name: ")
if not A or not B:
    print("Error: Both first name and last name must be provided.") 
else:
    print("Welcome",A,B)   
#this part checks if the credentials (username, password) are correct.
username = "admin" 
password = "password123"
usr = input("Please enter your username: ")
psw = input("Please enter your password: ")
if usr != username and psw != password:
    print("Error: Invalid login credentials")
elif usr == username and psw == password:
    print("Login successful.")
elif usr != username:
    print("Error: Invalid username.")
elif psw != password:
    print("Error: Invalid password.")