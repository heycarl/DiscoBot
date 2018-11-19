import sqlite3
connection = sqlite3.connect('disco.db', check_same_thread=False)
cursor = connection.cursor()

def create_db():
    try:
        cursor.execute("CREATE TABLE Users(Code INT, Name TEXT, Status INT)")
        print("DB created")
    except sqlite3.OperationalError:
        print("DB is already created")

def create_admin_db():
    try:
        cursor.execute("CREATE TABLE Admins(Code INT, Name TEXT, Money INT)")
        print("Admin DB created")
    except sqlite3.OperationalError:
        print("Admin is already created")

def write_user_code(code):
    cursor.execute(f"insert into Users values ({code}, 'Sasha', 1) ")
    connection.commit()

def write_admin_code(code):
    cursor.execute(f"insert into Users values ({code}, 'Sasha', 1) ")
    connection.commit()

def check_user_code(code):
    cursor.execute("SELECT Code FROM Users")
    row = cursor.fetchall()
    for item in row:
        if item[0] == code:
            return 1
        else:
            pass
    return 0

def check_admin_code(code):
    print(code)
    cursor.execute("SELECT Code FROM Admins")
    row = cursor.fetchall()
    for item in row:
        if item[0] == code:
            return 1
        else:
            pass
    return 0