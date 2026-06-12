import bcrypt

stored_password = bcrypt.hashpw(
    b"StrongPassword@123",
    bcrypt.gensalt()
)

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == "admin" and bcrypt.checkpw(password.encode(), stored_password):
    print("Login Successful")
else:
    print("Login Failed")