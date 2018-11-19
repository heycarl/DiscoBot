from random import randint
import db_functions

def generate_code():
    db_functions.create_db()
    while True:
        num = generate_numbers()
        if db_functions.check_user_code(num) == 0:
            break
        else:
            pass
    db_functions.write_user_code(num)
    return num

def generate_admin_code():
    db_functions.create_admin_db()
    while True:
        num = generate_numbers()
        if db_functions.check_admin_code(num) == 0:
            break
        else:
            pass
    db_functions.write_admin_code(num)
    return num

def generate_numbers():
    range_start = 10 ** (4 - 1)
    range_end = (10 ** 4) - 1
    return randint(range_start, range_end)