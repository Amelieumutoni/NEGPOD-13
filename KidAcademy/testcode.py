#!/usr/bin/python3

def display_exam_results(students_scores):
    # Iterate through each student
    for student, score in students_scores.items():
        # Display student's score
        print(f"\nStudent: {student}")
        print(f"Score: {score}")

        # Provide feedback based on the score
        if score >= 90:
            feedback = "Good effort, but there's room for improvement."
        elif 80 <= score < 90:
            feedback = "Great job! You're doing well."
        elif 70 <= score < 80:
            feedback = "Good effort, but there's room for improvement."
        else:
            feedback = "Keep working hard and you'll see progress."

        # Display personalized feedback
        print(f"Feedback: {feedback}")

# Example usage:
students_scores = {
    'Student1': 95,
    'Student2': 78,
    'Student3': 88,
    'Student4': 62,
    'Student5': 100,
}

display_exam_results(students_scores)

