from mysql.connector import Error

# Add a user
def add_user(conn, username, email, address, cell):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO users (username, email, address, cell)
            VALUES (%s, %s, %s, %s)
        ''', (username, email, address, cell))
        conn.commit()
        print("User added successfully!")
    except Error as e:
        print(f"Error adding user: {e}")
    finally:
        cursor.close()


# Edit a user
def edit_user(conn, user_id, new_username, new_email, new_address, new_cell):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE users
            SET username = %s, email = %s, address = %s, cell = %s
            WHERE id = %s
        ''', (new_username, new_email, new_address, new_cell, user_id))
        conn.commit()
        print("User updated successfully!")
    except Error as e:
        print(f"Error updating user: {e}")
    finally:
        cursor.close()


# Delete a user
def delete_user(conn, user_id):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM users
            WHERE id = %s
        ''', (user_id,))
        conn.commit()
        print("User deleted successfully!")
    except Error as e:
        print(f"Error deleting user: {e}")
    finally:
        cursor.close()
