import sqlite3

CREATE_DATABASE = "CREATE TABLE IF NOT EXISTS users (sitio_web TEXT, username TEXT, password TEXT)"
INSERT_USER = "INSERT INTO users (sitio_web, username, password) VALUES (?, ?, ?)"
SELECT_USER = "SELECT * FROM users"

connection = sqlite3.connect("C:/Users/NoteBook/data.db")

def add_user(website, user, password):
    with connection:
        connection.execute(INSERT_USER,(website, user, password))

def get_user():
    pass