import sqlite3

def get_user(user_input):

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username = ?",
        (user_input,)
    )

    return cursor.fetchall()
