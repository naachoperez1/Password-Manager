import sqlite3

CREATE_DATABASE = "CREATE TABLE IF NOT EXISTS users (web_site TEXT, username TEXT, password TEXT)"
INSERT_USER = "INSERT INTO users (web_site, username, password) VALUES (?, ?, ?)"
SELECT_USER = "SELECT * FROM users"
connection = sqlite3.connect("C:\Users\NoteBook\data.db")