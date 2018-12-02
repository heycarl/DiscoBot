import sqlite3
connection = sqlite3.connect('disco.db', check_same_thread=False)
cursor = connection.cursor()

def create_db():
    try:
        cursor.execute("CREATE TABLE Users(Code INT, Name TEXT, Status INT, Money INT, Parent INT)")
        print("DB created")
    except sqlite3.OperationalError:
        print("DB is already created")

def create_admin_db():
    try:
        cursor.execute("CREATE TABLE Admins(Code INT, Name TEXT, Money INT)")
        print("Admin DB created")
    except sqlite3.OperationalError:
        print("Admin is already created")

def write_user_code(code, name):
    cursor.execute(f"""insert into Users values ({code}, "{name}", 0, 0, 0) """)
    connection.commit()

def write_admin_code(code):
    cursor.execute(f"insert into Admins values ({code}, 'Sasha', 1) ")
    connection.commit()

def check_user_code(code):
    try:
        cursor.execute("SELECT Code FROM Users")
        row = cursor.fetchall()
        for item in row:
            if item[0] == code:
                return 1
            else:
                pass
        return 0
    except sqlite3.OperationalError:
        return 0

def check_user_pay(code):
    try:
        cursor.execute(f"SELECT * FROM Users WHERE Code LIKE '%{str(code)}%';")
        row = cursor.fetchall()
        row = list(row[0])[2]
        if row != 0:
            st = """С твоим статусом все отлично, желаем хорошо оторваться на дискотеке"""
        else:
            st = """На данный момент ты не можешь пройти на дискотеку, в ближайшее время найди организаторов ( Дима Сивашко 10 ''A'', Артур Демьянченко 11 "A" )"""
        return st
    except IndexError:
        return """Такого пользователя не существет"""

def update_user_pay(code):
    try:
        cursor.execute("SELECT Code FROM Users")
        row = cursor.fetchall()
        for item in row:
            if item[0] == int(code):
                sql = f"""
                    UPDATE Users 
                    SET Status = '{str(7)}' 
                    WHERE Code = '{str(code)}'
                    """
                cursor.execute(sql)
                connection.commit()
                return "Успешно изменено"
            else:
                pass
        return "Такого пользователя не существет"
    except sqlite3.OperationalError:
        return "Ошибка в БД. Если вы это видете, значит все печально и нужно написать @afimchik"

def check_admin_code(code):
    try:
        cursor.execute("SELECT Code FROM Admins")
        row = cursor.fetchall()
        for item in row:
            if item[0] == code:
                return 1
            else:
                pass
        return 0
    except sqlite3.OperationalError:
        return 0