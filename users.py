import sqlite3  # Database
from hashlib import sha512  # Hashing for Passwords
from uuid import uuid4  # Salting for Passwords
from re import search  # Regex


def create_user(username, password, repeat_pass, email):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = 'CREATE TABLE IF NOT EXISTS organization (user_id INT, username TEXT, password INT, salt INT, email TEXT)'
    c.execute(q)
    q = 'SELECT username, email FROM organization'
    users = c.execute(q)
    if username in users:
        return [False, "Username already taken."]
    if password != repeat_pass:
        return [False, "Passwords do not match."]
    if len(password) < 8:
        return [False, "Password too short."]
    if not (bool(search(r'\d', password)) and bool(search('[a-z]', password)) and bool(search('[A-Z]', password)) and bool(search(r'[!@#$%^*]', password))):
                return [False, "Your password must include a lowercase letter, an uppercase letter, a number, and at least of one the following symbols: '!@#$%^*'."]
    salt = uuid4().hex
    hash_password = sha512((password + salt) * 10000).hexdigest()
    q = 'SELECT COUNT(*) FROM parent_database'
    num_rows = c.execute(q).fetchone()[0]
    q = 'INSERT INTO parent_database (user_id, username, password, salt, email) VALUES (?, ?, ?, ?, ?)'
    c.execute(q, (num_rows + 1, username, hash_password, salt, email))
    conn.commit()
    conn.close()
    return [True, "Successful Account Creation"]


def valid_login(username, password):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = 'SELECT name FROM sqlite_master WHERE TYPE = "table" AND NAME = "organization"'
    c.execute(q)
    if not c.fetchone():
        conn.close()
        return -1
    q = 'SELECT password, salt FROM organization WHERE username = ?'
    pepper_and_salt = c.execute(q, (username,)).fetchone()
    if pepper_and_salt and sha512((password + pepper_and_salt[1]) * 10000).hexdigest() == pepper_and_salt[0]:
        q = "SELECT parent_id FROM organization WHERE username = ?"
        id = c.execute(q, (username,)).fetchone()
        conn.close()
        return id[0]
    conn.close()
    return -1
