#!/usr/bin/python3


import random

def display_course():
    course_title = "Rwandan Culture Course"
    course_description = "This course will provide an introduction to the Rwandan culture. You will learn about the customs, traditions, and values that shape Rwandan culture. You will also have the opportunity to practice the local language and learn about the unique geographical features of Rwanda."

    culture = {
        "name": "Rwanda",
        "customs": ["Respect for Elders", "Politeness", "Family is important"],
        "traditions": ["Umuganda", "Rural Housing", "Burial Traditions"],
        "geographical_features": ["Mountain ranges", "Lakes", "Forests"],
        "language": "Kinyarwanda",
        "image": "rwanda.jpg"
    }

    print("Course Title: " + course_title)
    print("Course Description: " + course_description)
    print("")
    print("Culture Name: " + culture["name"])
    print("Customs: ")
    for custom in culture["customs"]:
        print("- " + custom)
    print("Traditions: ")
    for tradition in culture["traditions"]:
        print("- " + tradition)
    print("Geographical Features: ")
    for feature in culture["geographical_features"]:
        print("- " + feature)
    print("Language: " + culture["language"])
    print("Image: " + culture["image"])

def generate_custom_exercise():
    """Generate a custom exercise with a string question and answer."""
    question = "Agapfundikiye gatera...?"
    answer = "amatsiko"
    return question, answer

def check_answer(user_answer, correct_answer):
    """Check if the user's answer is correct."""
    return user_answer.lower() == correct_answer.lower()

def update_level(score):
    """Update the user's level based on the score."""
    if score >= 3:
        return "Intermediate"
    elif score >= 6:
        return "Advanced"
    else:
        return "Beginner"

def register_user(users):
    """Register a new user."""
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    # Check if the username is already taken
    if username in users:
        print("Username already taken. Please choose a different one.")
    else:
        users[username] = password
        print("Registration successful!")

def login_user(users):
    """Login an existing user."""
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username and password match
    if username in users and users[username] == password:
        print("Login successful!")
        return username
    else:
        print("Invalid username or password. Please try again.")
        return None

def main():
    users = {}  # Dictionary to store user credentials
    scores = {}  # Dictionary to store user scores
    levels = {}  # Dictionary to store user levels
    current_user = None  # To keep track of the currently logged-in user

    while True:
        # Display options
        print("Options:")
        print("1. Register")
        print("2. Login")
        print("3. View Courses")
        print("4. Practice Tests")
        print("5. View Scores")
        print("6. View Levels")
        print("7. Quit")

        # Get user input for option
        option = input("Choose an option (1, 2, 3, 4, 5, 6, or 7): ")

        if option == "1":
            # Register a new user
            register_user(users)
        elif option == "2":
            # Login an existing user
            current_user = login_user(users)
        elif option == "3":
            # Display the course information
            display_course()
        elif option == "4":
            if current_user is not None:
                # Generate a custom exercise
                question, correct_answer = generate_custom_exercise()

                while True:
                    # Display the exercise and get user input
                    user_input = input(question + " ")

                    # Check the user's answer
                    if check_answer(user_input, correct_answer):
                        print("Correct! Good job.")
                        # Update the user's score
                        scores[current_user] = scores.get(current_user, 0) + 1
                        # Update the user's level
                        levels[current_user] = update_level(scores[current_user])
                        break  # Exit the loop if the answer is correct
                    else:
                        print("Sorry, the answer is incorrect. Please try again.")
            else:
                print("Please log in before practicing tests.")
        elif option == "5":
            # View scores
            print("Scores:")
            for user, score in scores.items():
                print(f"{user}: {score} points")
        elif option == "6":
            # View levels
            print("Levels:")
            for user, level in levels.items():
                print(f"{user}: {level}")
        elif option == "7":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, 4, 5, 6, or 7.")

if __name__ == "__main__":
    main()
