import sqlite3

def create_table():
    """
    Creates qr_history table if it doesn't exist.
    """

    conn = sqlite3.connect("qr_history.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS qr_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT NOT NULL,
        qr_color TEXT,
        bg_color TEXT,
        filename TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

