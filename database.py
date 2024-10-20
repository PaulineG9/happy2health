import sqlite3

def connect_db():
    return sqlite3.connect("user_data.db")

def create_user(name, email, user_type, tracking, check_in_freq, contact_method):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            name TEXT, 
            email TEXT, 
            user_type TEXT, 
            tracking TEXT, 
            check_in_freq TEXT, 
            contact_method TEXT
        )
    """)
    cursor.execute(
        "INSERT INTO users (name, email, user_type, tracking, check_in_freq, contact_method) VALUES (?, ?, ?, ?, ?, ?)",
        (name, email, user_type, ", ".join(tracking), check_in_freq, contact_method)
    )
    conn.commit()
    conn.close()

def get_user(email):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email=?", (email,))
    user = cursor.fetchone()
    conn.close()
    return user
