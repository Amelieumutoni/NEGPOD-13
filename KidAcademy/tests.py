#!/usr/bin/python3

import random

def generate_custom_exercise():
    """Generate a custom exercise with a string question and answer."""
    question = "Agapfundikiye gatera...?"
    answer = "amatsiko"
    return question, answer

def check_answer(user_answer, correct_answer):
    """Check if the user's answer is correct."""
    return user_answer.lower() == correct_answer.lower()

def main():
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

if __name__ == "__main__":
    main()
