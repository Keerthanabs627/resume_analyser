import sqlite3

def create_table():
    conn = sqlite3.connect("resumes.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS candidates(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        phone TEXT,
        skills TEXT,
        score INTEGER,
        resume_text TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_candidate(email, phone, skills, score, resume_text):
    conn = sqlite3.connect("resumes.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO candidates
    (email, phone, skills, score, resume_text)
    VALUES (?, ?, ?, ?, ?)
    """, (email, phone, skills, score, resume_text))

    conn.commit()
    conn.close()

def get_all_candidates():
    conn = sqlite3.connect("resumes.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM candidates")
    data = cursor.fetchall()

    conn.close()
    return data