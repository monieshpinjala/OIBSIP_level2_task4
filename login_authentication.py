!pip install bcrypt
import bcrypt

user_data = {}

def register_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    user_data[username] = hashed_password
    print("Registration successful!")

def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in user_data:
        stored_password = user_data[username]
        if bcrypt.checkpw(password.encode(), stored_password):
            print("Login successful!")
            access_secured_page()
            return
    print("Invalid username or password.")

def access_secured_page():
    print("Welcome to the secured page!")
    print("You Are Selected For Oasis Infobyte Internship")

# Example usage
register_user()
login_user()
