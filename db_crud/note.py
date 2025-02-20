from mysql.connector import Error
import json

# Add a note
def add_note(conn, title, content, hashtags, tagged_users):
    try:
        cursor = conn.cursor()
        # Convert lists to JSON strings
        hashtags_json = json.dumps(hashtags)
        tagged_users_json = json.dumps(tagged_users)
        cursor.execute('''
                    INSERT INTO notes (title, content, hashtags, tagged_users)
                    VALUES (%s, %s, %s, %s)
                ''', (title, content, hashtags_json, tagged_users_json))
        conn.commit()
        print("Note added successfully!")
    except Error as e:
        print(f"Error adding note: {e}")
    finally:
        cursor.close()

# Edit a note
def edit_note(conn, note_id, new_title, new_content, new_hashtags, new_tagged_users):
    try:
        cursor = conn.cursor()
        # Convert lists to JSON strings
        new_hashtags_json = json.dumps(new_hashtags)
        new_tagged_users_json = json.dumps(new_tagged_users)
        cursor.execute('''
                    UPDATE notes
                    SET title = %s, content = %s, hashtags = %s, tagged_users = %s
                    WHERE id = %s
                ''', (new_title, new_content, new_hashtags_json, new_tagged_users_json, note_id))
        conn.commit()
        print("Note updated successfully!")
    except Error as e:
        print(f"Error updating note: {e}")
    finally:
        cursor.close()


# Delete a note
def delete_note(conn, note_id):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM notes
            WHERE id = %s
        ''', (note_id,))
        conn.commit()
        print("Note deleted successfully!")
    except Error as e:
        print(f"Error deleting note: {e}")
    finally:
        cursor.close()
