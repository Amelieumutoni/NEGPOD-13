#!/usr/bin/python3
"""
Starting of a new project
"""
import hashlib
import mysql.connector
from validation import validate_username, validate_password

database_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': '',
    'port': 3306  # Add the port parameter with the correct port number
}

try:
    connection = mysql.connector.connect(**database_config)
except mysql.connector.Error as err:
    print(f"Error: {err}")

users = {}


def register():
    print("Register a new account:")
    username = input("Enter your username: ")

    # Check if the username already exists
    if username in users:
        print("Username already exists. Please choose a different one.")
        return  # Correct indentation here

    password = input("Enter your password: ")

    # The password before storing it
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    users[username] = {
        "password": hashed_password,
        "content": []
    }

    print("Registration successful.")


def login():
    print("Login to your account:")
    username = input("Enter your username: ")

    # Check if the username exists
    if username not in users:
        print("Username not found. Please register.")
        return

    password = input("Enter your password: ")

    # Compare the entered password with the stored
    entered_password_hash = hashlib.sha256(password.encode()).hexdigest()
    if entered_password_hash == users[username]["password"]:
        print("Login successful.")
        return username
    else:
        print("Incorrect password.")


def create_content(current_user):
    print(f"User '{current_user}' - Create content:")
    content_text = input("Enter your content: ")

    users[current_user]["content"].append(content_text)

    print("Content created successfully.")


def view_content():
    print("Viewing content:")
    for username, data in users.items():
        for content in data["content"]:
            print(f"{username}: {content}")


def main():
    current_user = None

    while True:
        print("\nOptions:")
        print("1. Register")
        print("2. Login")
        print("3. Create Content")
        print("4. View Content")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            register()
        elif choice == "2":
            current_user = login()
        elif choice == "3":
            if current_user:
                create_content(current_user)
            else:
                print("Please log in first.")
        elif choice == "4":
            view_content()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
