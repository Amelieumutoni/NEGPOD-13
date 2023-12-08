#!/usr/bin/python3

import random
import os

def generate_custom_exercise():
    """Generate a custom exercise with a string question and answer."""
    question = "Agapfundikiye gatera...?"
    answer = "amatsiko"
    return question, answer

def check_answer(user_answer, correct_answer):
    """Check if the user's answer is correct."""
    return user_answer.lower() == correct_answer.lower()

def open_another_file():
    file_path = '/root/NEGPOD-13/KidAcademy/welcome.py'
    os.system('xdg-open ' + file_path)

def take_test():
    """Function to take a test."""
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

def main():
    while True:
        print("Menu:")
        print("1. Take a test")
        print("2. Return to home page")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            take_test()
        elif choice == "2":
            user_input = input("Press 'r' to open another file: ")
            if user_input.lower() == 'r':
                open_another_file()
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
