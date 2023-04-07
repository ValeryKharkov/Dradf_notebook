import sqlite3 as sl

con = sl.connect('test_db_SQLiteStudio', check_same_thread=False)

cursor = con.cursor()

def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
	cursor.execute('INSERT INTO users (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)', (user_id, user_name, user_surname, username))
	con.commit()