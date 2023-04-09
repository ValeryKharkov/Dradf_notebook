import sqlite3


def read_sqlite_table():
    try:
        sqlite_connection = sqlite3.connect('test_db.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_select_query = """SELECT * from humans"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Всего строк:  ", len(records))
        print("Вывод каждой строки")
        for row in records:
            print("ID:", row[0])
            print("Имя:", row[1])
            print("Фамилия:", row[2])
            print("Пол:", row[3], end="\n\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

# read_sqlite_table()


def search_object(text, search_type):
    object_info = []  # готовим выходное представление
    connect = sqlite3.connect('test_db.db')
    cursor = connect.cursor()
    print("Подключен к SQLite")
    # здесь поиск по базе
    if search_type == 'номер':
        # алгоритм поиска по кадастровому номеру в БД
        sql_query = """select * from humans where human_id = ?"""
        cursor.execute(sql_query, (text),)
        records = cursor.fetchall()
        print(records)
    cursor.close()


search_object('5', 'номер')

    # elif search_type == 'адрес':
    #     pass  # алгоритм поиска по адресу в БД
    # if text in sql:  # готовим нужный вариант вывода, если text в базе
    #     object_info.append(0)
    #     object_info.append('данные из БД')
    # else:  # если в БД не находится нужный объект, выдаём код ошибки
    #     object_info.append(1)
    # return object_info
