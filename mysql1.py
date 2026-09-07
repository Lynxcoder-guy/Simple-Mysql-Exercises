import mysql.connector
import time

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jakarta1#%",
    database="first_database"
)

cursor = conn.cursor()

# bikin tabel users kalau belum ada
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
)
""")

while True:
    print("hello welcome to the program test")
    time.sleep(1)
    instructions = input("Enter your instructions (1. ADD, 2. DELETE, 3. SEE): ")
    if instructions == "1":
        name = input("Enter name: ")
        email = input("Enter email: ")
        sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
        val = (name, email)
        cursor.execute(sql, val)
        conn.commit()
        print("User added successfully.")
    elif instructions == "2":
        user_id = input("Enter user ID to delete: ")
        sql = "DELETE FROM users WHERE id = %s"
        val = (user_id,)
        cursor.execute(sql, val)
        conn.commit()
        print("User deleted successfully.")
    elif instructions == "3":
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        for user in users:
            print(user)
    else:
        print("Invalid instruction.")

#sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
#val = ("Lynxguy", "lynxguy@example.com")
#cursor.execute(sql, val)

