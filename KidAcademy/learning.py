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

def main():
    while True:
        # Display options
        print("Options:")
        print("1. View Courses")
        print("2. Practice Tests")
        print("3. Quit")

        # Get user input for option
        option = input("Choose an option (1, 2, or 3): ")

        if option == "1":
            # Display the course information
            display_course()
        elif option == "2":
            # Generate a custom exercise
            question, correct_answer = generate_custom_exercise()

            while True:
                # Display the exercise and get user input
                user_input = input(question + " ")

                # Check the user's answer
                if check_answer(user_input, correct_answer):
                    print("Correct! Good job.")
                    break  # Exit the loop if the answer is correct
                else:
                    print("Sorry, the answer is incorrect. Please try again.")
        elif option == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
