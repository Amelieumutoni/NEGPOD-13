#!/usr/bin/python3

from database_manager import DatabaseManager

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

def main():
    db_manager = DatabaseManager()
    current_user = None

    try:
        while True:
            print("Options:")
            print("1. Register")
            print("2. Login")
            print("3. View Courses")
            print("4. Practice Tests")
            print("5. View Scores")
            print("6. View Levels")
            print("7. Quit")

            option = input("Choose an option (1, 2, 3, 4, 5, 6, or 7): ")

            try:
                if option == "1":
                    username = input("Enter a username: ")
                    password = input("Enter a password: ")
                    db_manager.register_user(username, password)
                elif option == "2":
                    username = input("Enter your username: ")
                    password = input("Enter your password: ")
                    current_user = db_manager.login_user(username, password)
                elif option == "3":
                    display_course()
                elif option == "4":
                    if current_user is not None:
                        question, correct_answer = generate_custom_exercise()

                        while True:
                            user_input = input(question + " ")

                            if check_answer(user_input, correct_answer):
                                print("Correct! Good job.")
                                db_manager.update_score(current_user, 1)
                                db_manager.update_level(current_user, update_level(1))
                                break
                            else:
                                print("Sorry, the answer is incorrect. Please try again.")
                    else:
                        print("Please log in before practicing tests.")
                elif option == "5":
                    print("Scores:")
                    scores_data = db_manager.get_scores_data()
                    for user, score in scores_data:
                        print(f"{user}: {score} points")
                elif option == "6":
                    print("Levels:")
                    levels_data = db_manager.get_levels_data()
                    for user, level in levels_data:
                        print(f"{user}: {level}")
                elif option == "7":
                    print("Exiting the program. Goodbye!")
                    db_manager.close_connection()
                    break
                else:
                    print("Invalid option. Please choose 1, 2, 3, 4, 5, 6, or 7.")
            except Exception as e:
                print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
