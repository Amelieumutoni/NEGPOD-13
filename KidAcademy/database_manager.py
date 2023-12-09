#!/usr/bin/python3

import sqlite3

class DatabaseManager:
    def __init__(self, db_file='culture_course.db'):
        self.conn = sqlite3.connect(db_file)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()

        # Create Users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')

        # Create Scores table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                score INTEGER NOT NULL,
                FOREIGN KEY(user_id) REFERENCES Users(id)
            )
        ''')

        # Create Levels table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Levels (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                level TEXT NOT NULL,
                FOREIGN KEY(user_id) REFERENCES Users(id)
            )
        ''')

        self.conn.commit()

    def register_user(self, username, password):
        cursor = self.conn.cursor()

        # Check if the username is already taken
        cursor.execute('SELECT id FROM Users WHERE username = ?', (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            print("Username already taken. Please choose a different one.")
        else:
            cursor.execute('INSERT INTO Users (username, password) VALUES (?, ?)', (username, password))
            self.conn.commit()
            print("Registration successful!")

    def login_user(self, username, password):
        cursor = self.conn.cursor()

        cursor.execute('''
            SELECT id FROM Users
            WHERE username = ? AND password = ?
        ''', (username, password))

        user_id = cursor.fetchone()

        if user_id:
            print("Login successful!")
            return user_id[0]
        else:
            print("Invalid username or password. Please try again.")
            return None

    def update_level(self, user_id, level):
        cursor = self.conn.cursor()

        cursor.execute('''
            INSERT OR REPLACE INTO Levels (user_id, level)
            VALUES (?, ?)
        ''', (user_id, level))

        self.conn.commit()

    def update_score(self, user_id, score):
        cursor = self.conn.cursor()

        cursor.execute('''
            INSERT OR REPLACE INTO Scores (user_id, score)
            VALUES (?, ?)
        ''', (user_id, score))

        self.conn.commit()

    def get_scores_data(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT username, score FROM Users JOIN Scores ON Users.id = Scores.user_id')
        return cursor.fetchall()

    def get_levels_data(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT username, level FROM Users JOIN Levels ON Users.id = Levels.user_id')
        return cursor.fetchall()

    def close_connection(self):
        self.conn.close()
