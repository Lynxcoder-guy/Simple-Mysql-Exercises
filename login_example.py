import mysql.connector as mysql
import time
import re

# Establish a connection to the MySQL database
conn = mysql.connect(
    host="localhost",
    user="root",
    password="Jakarta1#%",
    database="login_example"
)

cursor = conn.cursor()

def check_email_format(email):
    # Regular expression for validating an Email
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(regex, email):
        return True
    else:
        return False

while True:
    print("Welcome to the login program")
    time.sleep(1)
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100)
    )""")
    instructions = input("Enter your instructions (1. LOGIN, 2. REGISTER, 3. VIEW USERS): ")
    if instructions == "1":
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        # Check if the email exists in the database
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        if user:
            # Assuming the password is stored in the database, you would check it here
            # For this example, we will just print a success message
            print("Login successful!")
        else:
            print("Email not found. Please register first.")
    elif instructions == "2":
        name = input("Enter your name: ")   
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        # Validate email format
        if not check_email_format(email):
            print("Invalid email format. Please try again later.")
        else:
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            user = cursor.fetchone()
            if user:
                print("Email already exists. Please try again later.")
            else:
                #insert the data for a new user into the database
                sql = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
                val = (name, email, password)
                cursor.execute(sql, val)
                conn.commit()
                print("User registered successfully.")
    elif instructions == "3":
        cursor.execute("""SELECT * FROM users""")
        users = cursor.fetchall()
        for user in users:
            print(user)
