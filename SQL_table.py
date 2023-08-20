# Q. Write a Python code to configure the MySQL Connector in your system and Insert data to
# MySQL Table after which you Fetch and Display data from Table
import mysql.connector

# Configure database connection
db_config = {
    "host": "localhost",
    "user": "Prince", # your_username
    "password": "tiger123", # your_password
    "database": "python" # your_database_name
}

# Establish a connection
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Create a table (if it doesn't exist)
create_table_query = """
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT
)
"""
cursor.execute(create_table_query)
connection.commit()

# Insert data into the table
insert_query = "INSERT INTO students (name, age) VALUES (%s, %s)"
data_to_insert = [("Alice", 25), ("Bob", 30), ("Charlie", 22)]
cursor.executemany(insert_query, data_to_insert)
connection.commit()

# Fetch and display data from the table
select_query = "SELECT * FROM students"
cursor.execute(select_query)
students = cursor.fetchall()

print("Fetched data:")
for student in students:
    print("ID:", student[0])
    print("Name:", student[1])
    print("Age:", student[2])
    print()

# Close the cursor and connection
cursor.close()
connection.close()
