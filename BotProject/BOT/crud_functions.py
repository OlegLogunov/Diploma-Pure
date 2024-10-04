import sqlite3

def initiate_db():
    connection = sqlite3.connect("IntCard.db")
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Pictures(
    id INTEGER PRIMARY KEY,
    pict BLOB NOT NULL,
    description TEXT
    )
    ''')
    connection.commit()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    login TEXT NOT NULL,
    password TEXT NOT NULL
    )
    ''')
    connection.commit()
    connection.close()


def get_all_pictures():
    connection = sqlite3.connect("IntCard.db")
    cursor = connection.cursor()

    cursor.execute("SELECT pict, description FROM Pictures")
    users = cursor.fetchall()


    connection.commit()
    connection.close()
    return users


def add_user(login, password):
    connection = sqlite3.connect("IntCard.db")
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM Users")
    total_us = cursor.fetchone()[0]+1
    cursor.execute(f'''
    INSERT INTO Users VALUES('{total_us}', '{login}', '{password}')
    ''')

    connection.commit()
    connection.close()


def is_included(login, password):
    connection = sqlite3.connect("IntCard.db")
    cursor = connection.cursor()

    is_inc = True
    check_logpass = cursor.execute("SELECT * FROM Users WHERE login = ? AND password = ?", (login, password))
    if check_logpass.fetchone() is None:
        is_inc = False

    return is_inc


    connection.commit()
    connection.close()

initiate_db()