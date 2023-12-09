#!/usr/bin/python3

import mysql.connector

# Database configuration
database_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'your_database_name',  # Replace with your actual database name
}

# Establish a connection to the database
connection = mysql.connector.connect(**database_config)

def read_scores_from_file(file_path):
    """
    Read scores from a file and return a list of scores.

    Parameters:
    - file_path (str): Path to the file containing scores.

    Returns:
    - list: List of scores.
    """
    with open(file_path, 'r') as file:
        scores = [int(line.strip()) for line in file]
    return scores

def read_level_from_file(file_path):
    """
    Read the level from a file and return the level.

    Parameters:
    - file_path (str): Path to the file containing the level.

    Returns:
    - int: Level.
    """
    with open(file_path, 'r') as file:
        level = int(file.read().strip())
    return level

def store_user_info(username, scores_file, level_file):
    """
    Store user information in a MySQL database.

    Parameters:
    - username (str): The username of the user.
    - scores_file (str): Path to the file containing scores.
    - level_file (str): Path to the file containing the level.
    """
    # Read scores and level from files
    scores = read_scores_from_file(scores_file)
    level = read_level_from_file(level_file)

    cursor = connection.cursor()

    # Insert user information into the 'users' table (assuming such a table exists)
    insert_query = "INSERT INTO users (username, scores, level) VALUES (%s, %s, %s)"
    user_data = (username, str(scores), str(level))

    cursor.execute(insert_query, user_data)

    # Commit the changes and close the cursor
    connection.commit()
    cursor.close()
