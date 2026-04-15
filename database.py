import sqlite3
from datetime import datetime
from security import hash_password

DB_NAME = "saas.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # USERS
    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT,
        plan TEXT,
        usage INTEGER DEFAULT 0
    )
    """)

    # CLIENTS
    c.execute("""
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT,
        age INTEGER,
        revenu REAL,
        couverture REAL,
        risque REAL,
        prime REAL,
        date TEXT
    )
    """)

    # ADMIN AUTO
    try:
        c.execute(
            "INSERT INTO users (username, password, role, plan) VALUES (?, ?, ?, ?)",
            ("admin", hash_password("admin123"), "admin", "enterprise")
        )
    except:
        pass

    conn.commit()
    conn.close()


def create_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    try:
        c.execute(
            "INSERT INTO users (username, password, role, plan) VALUES (?, ?, ?, ?)",
            (username, hash_password(password), "client", "free")
        )
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()


def get_user(username):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username=?", (username,))
    user = c.fetchone()

    conn.close()
    return user


def increment_usage(username):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("UPDATE users SET usage = usage + 1 WHERE username=?", (username,))
    conn.commit()
    conn.close()


def save_client(user, age, revenu, couverture, risque, prime):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
    INSERT INTO clients (user, age, revenu, couverture, risque, prime, date)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (user, age, revenu, couverture, risque, prime, datetime.now()))

    conn.commit()
    conn.close()


def get_clients():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("SELECT * FROM clients")
    data = c.fetchall()

    conn.close()
    return data