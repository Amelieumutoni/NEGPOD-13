"""
Starting of new project
"""
#!/usr/bin/env python

import hashlib

import mysql.connector
database_config = {
    'host':'localhost',
    'user':'root',
    'password':'',
    'database':'',
}
try:
    connection = mysql.connector.connect(**database_config)

user_name = input("Enter your username");


users = {}


def register():
    print("Register a new account:")
    username = input("Enter your username: ")

    # Check if the username already exists
    if username in users:
        print("Username already exists. Please choose a different one.")
        return

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
    [200~def view_content():
                print("Viewing content:")
                    for username, data in users.items():
                            for content in data["content"]:
                                        print(f"{username}: {content}")


                                        def main():
                                            current_user = None

