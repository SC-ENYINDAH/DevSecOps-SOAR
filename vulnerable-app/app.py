import sqlite3

def get_user(user_input):

    conn = sqlite3.connect("users.db")

    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username = ?"

    cursor.execute(query,(user_input,))

    return cursor.fetchall()
