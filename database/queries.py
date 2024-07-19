import sqlite3


def insert_user_to_languages_table(chat_id):
    database = sqlite3.connect("anime.db")
    cursor = database.cursor()

    cursor.execute("""
    INSERT OR IGNORE INTO languages(chat_id)
    VALUES (?)
    """, (chat_id,))

    database.commit()
    database.close()


def update_user_language(chat_id, language):
    database = sqlite3.connect("anime.db")
    cursor = database.cursor()
    cursor.execute("""
    UPDATE languages
    SET language = ?
    WHERE chat_id = ?
    """, (language, chat_id))
    database.commit()
    database.close()


def get_user_language(chat_id):
    database = sqlite3.connect("anime.db")
    cursor = database.cursor()
    cursor.execute("""
    SELECT language FROM languages
    WHERE chat_id = ?
    """, (chat_id,))
    language = cursor.fetchone()[0]
    database.commit()
    database.close()
    return language


def get_all_years():
    database = sqlite3.connect("anime.db")
    cursor = database.cursor()
    cursor.execute("""
    SELECT year_id, year FROM years;
    """)
    years = cursor.fetchall()
    database.commit()
    database.close()
    years = [year for year in years]
    return years


def get_anime_by_year(year_id):
    database = sqlite3.connect("anime.db")
    cursor = database.cursor()
    cursor.execute("SELECT anime_id, title_eng FROM anime WHERE year = ?;", (year_id,))
    animes = cursor.fetchall()
    database.close()
    anime = [anime for anime in animes]
    return anime


def get_year_by_title(requested_year):
    database = sqlite3.connect("anime.db")
    cursor = database.cursor()
    cursor.execute("""
    SELECT year_id FROM years WHERE year = ?
    """, (requested_year, ))
    year = cursor.fetchone()[0]
    database.close()
    return year


def get_anime_data(anime_callback):
    anime_id = anime_callback.split("_")[1]
    database = sqlite3.connect("anime.db")
    cursor = database.cursor()
    cursor.execute("""
    SELECT year, title_eng, title_jap, synopsis FROM anime
    WHERE anime_id = ?
    """, (anime_id, ))

    anime_data = cursor.fetchone()[1:]

    return anime_data