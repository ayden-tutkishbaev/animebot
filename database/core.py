import sqlite3


def create_languages_table():
    database = sqlite3.connect("anime.db")
    cursor = database.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS languages(
        language_id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id INTEGER UNIQUE,
        language TEXT DEFAULT "")
    """)
    database.commit()
    database.close()


def create_years_table():
    database = sqlite3.connect("anime.db")
    cursor = database.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS years(
            year_id INTEGER PRIMARY KEY AUTOINCREMENT,
            year TEXT
        )
    """)
    database.commit()
    database.close()


def create_anime_table():
    database = sqlite3.connect("anime.db")
    cursor = database.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS anime(
            anime_id INTEGER PRIMARY KEY AUTOINCREMENT,
            year TEXT REFERENCES years(year_id),
            title_eng TEXT,
            title_jap TEXT,
            synopsis TEXT
        )
    """)
    database.commit()
    database.close()