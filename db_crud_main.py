from db_crud.note import add_note, edit_note, delete_note
from db_crud.user import add_user, edit_user, delete_user
from tables.sqls import connect_to_db, create_tables


# Main function
def main():
    conn = connect_to_db()
    if conn:
        create_tables(conn)

        # Add a user
        add_user(conn, "john_doe", "john@example.com", "123 Main St", "123-456-7890")

        # Add a note
        add_note(conn, "First Note", "This is the content of the note.", ["#python", "#postgres"], [1])

        # Edit a user
        edit_user(conn, 1, "john_doe_updated", "john_updated@example.com", "456 Elm St", "987-654-3210")

        # Edit a note
        edit_note(conn, 1, "Updated Note Title", "Updated content.", ["#updated"], [1])

        # Delete a note
      #  delete_note(conn, 2)

        # Delete a user
        delete_user(conn, 2)

        conn.close()

if __name__ == "__main__":
    main()