ck_and_update_level(user_score):
    # Define level thresholds
    beginner_threshold = 50
    intermediate_threshold = 100
    # Check user's score and update level
    if user_score < beginner_threshold:
        user_level = 'Beginner'
    elif beginner_threshold <= user_score < intermediate_threshold:
        user_level = 'Intermediate'
    else:
        user_level = 'Advanced'
    
    # Print the user's current level
    print(f"Your current level is: {user_level}")
    
    # Update the user's level based on performance
    if user_score >= intermediate_threshold:
        print("Congratulations! You've advanced to the next level.")
        # Update user's level to the next level
        if user_level == 'Beginner':
            user_level = 'Intermediate'
        elif user_level == 'Intermediate':
            user_level = 'Advanced'
    
    return user_level

# Example usage:
user_score = 75
current_user_level = track_and_update_level(user_score)
print(f"Updated level: {current_user_level}")

