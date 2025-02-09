import mysql.connector

# Try to connect to MySQL
try:
    # Connect to MySQL server (Change 'root' and 'your_password' to your actual username and password)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password"  # Replace with your MySQL password
    )

    # Create a cursor object to run SQL commands
    cursor = connection.cursor()

    # SQL command to create the database (if it doesn't exist)
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

    # Print success message
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    # Print error message if something goes wrong
    print(f"Error: {err}")

finally:
    # Always close the connection to MySQL
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed.")

