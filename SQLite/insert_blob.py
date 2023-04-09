import sqlite3

sqlite_connection = sqlite3.connect('sqlite_python.db')
cursor = sqlite_connection.cursor()
print("Подключен к SQLite_1")

cursor.execute(""" CREATE TABLE IF NOT EXISTS new_employee (
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
name TEXT NOT NULL, photo BLOB NOT NULL,
resume BLOB NOT NULL);""")
sqlite_connection.commit()


def convert_to_binary_data(filename):
    # Преобразование данных в двоичный формат
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data


def insert_blob(name, photo, resume_file):
    try:
        # sqlite_connection = sqlite3.connect('sqlite_python.db')
        # cursor = sqlite_connection.cursor()
        # print("Подключен к SQLite_2")

        sqlite_insert_blob_query = """INSERT OR IGNORE INTO new_employee
                                  (name, photo, resume) VALUES (?, ?, ?)"""

        emp_photo = convert_to_binary_data(photo)
        resume = convert_to_binary_data(resume_file)
        # Преобразование данных в формат кортежа
        data_tuple = (name, emp_photo, resume)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqlite_connection.commit()
        print("Изображение и файл успешно вставлены как BLOB в таблицу")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite: ", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


insert_blob("Smith", "blob_files/photo_1.jpg", "blob_files/document_1.docx")
insert_blob("David", "blob_files/photo_2.jpg", "blob_files/document_2.docx")

