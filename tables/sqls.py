import mysql.connector
from mysql.connector import Error
from config_utils import get_database_credentials

# Database connection details
DB_HOST = "localhost"
DB_PORT = "3306"

try:
    db_host, db_user, db_password = get_database_credentials()
except ValueError as e:
    print(f"Error: {e}")


# Connect to PostgreSQL
def connect_to_db():
    try:
        conn = mysql.connector.connect(
            database=db_host,
            user=db_user,
            password=db_password,
            host=DB_HOST,
            port=DB_PORT
        )
        return conn
    except Error as e:
        print(f"Error connecting to the database: {e}")
        return None

# Create tables
def create_tables(conn):
    try:
        cursor = conn.cursor()

        # Create users table
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        username VARCHAR(50) NOT NULL,
                        email VARCHAR(100) NOT NULL UNIQUE,
                        address TEXT,
                        cell VARCHAR(15),
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')

        # Create notes table
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS notes (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        title VARCHAR(100) NOT NULL,
                        content TEXT,
                        hashtags JSON,  # Using JSON for hashtags
                        tagged_users JSON,  # Using JSON for tagged users
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')

        conn.commit()
        print("Tables created successfully!")
    except Exception as e:
        print(f"Error creating tables: {e}")
    finally:
        cursor.close()