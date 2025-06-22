import mysql.connector as connector

connection = connector.connect(
    host="localhost",
    user="root",
    password="password24*"
)

if connection.is_connected():  # Removed extra space here
    print("successfully connected")
else:
    print("failed connection")
