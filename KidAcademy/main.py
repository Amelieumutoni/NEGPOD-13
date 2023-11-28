"""
Starting of new project
"""
#!/usr/bin/env python

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
