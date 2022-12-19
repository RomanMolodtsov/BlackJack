import sqlite3
import time, random

global db
global sql

tuz = 0
result = 0
tuz_crup = 0
res_crup = 0
number = 0

db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT,
    cash INT
)""")

db.commit()

def reg():
    user_login = input('Login: ')
    user_password = input('Password: ')

    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?,?,?)", (user_login, user_password, 0))
        db.commit()

        print('Зарегестрированно!')
    else:
        print('Такая запись уже имеется')

        for value in sql.execute("SELECT * FROM users"):
            print(value[0])


def delete_db():
    sql.execute(f"DELETE FROM users WHERE login = '{user_login}'")
    db.commit()

    print('Запись удалена!')

def first():
    global z
    global result
    global tuz
    z = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    if z == 11:
        tuz += 1
    result += z
    print(z)
    return result

def one_more():
    global x
    global result
    global tuz
    x = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    if x == 11:
        tuz += 1
    result += x
    if result > 21 and tuz > 0:
        result -= 10
        tuz -=1
    print(x)
    print(f'Твой счет {result}')
    if result > 21:
        print('Перебор! Ты проиграл!')
        number = 0

    return result

def crup():
    global y
    global res_crup
    global tuz_crup
    y = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    if y == 11:
        tuz_crup += 1
    res_crup += y
    print(y)
    return res_crup

def casino():
    global user_login
    global number
    user_login = input('Log in: ')

    for i in sql.execute(f"SELECT cash FROM users WHERE login = '{user_login}'"):
        #global balance
        balance = i[0]

    sql.execute(f'SELECT login FROM users WHERE login ="{user_login}"')
    if sql.fetchone() is None:
        print('Такого логина не существует. Зарегестрируй его.')
        reg()

    first()
    time.sleep(1)
    first()
    time.sleep(1)
    print(f'Твой счет {result}')

    while result < 21:
        a = input('Ещё? да/нет  ')
        if a == 'да':
            one_more()
        elif a == 'нет':
            print(f'Ты набрал {result}!')
            break
        if result == 21:
            print('Ты выиграл!!!')
            number = 1

    if result < 21:
        crup()
        time.sleep(1)
        crup()
        time.sleep(1)
        while res_crup < 22:
            if res_crup < 18:
                crup()
                time.sleep(1)
            elif res_crup > 17 and res_crup < 22:
                print(res_crup)
                break
            elif res_crup > 21:
                print(f'Я набрал {res_crup}, это перебор!')
                number = 1
                break
    if result > res_crup and result < 22:
        print('Ты выиграл!')
        number = 1
    elif result < res_crup and res_crup < 22:
        print('Ты проиграл!')
        number = 0
    elif res_crup > 21:
        print('Я перебрал! Ты победил!')
        number = 1
    elif result == res_crup and result < 22:
        print('Ничья!')
        number = 2
        sql.execute(f'UPDATE users SET cash = {balance + 0} WHERE login = "{user_login}"')
        db.commit()

    if number == 1:
        sql.execute(f'UPDATE users SET cash = {balance + 1000} WHERE login = "{user_login}"')
        db.commit()
    elif number == 2:
        sql.execute(f'UPDATE users SET cash = {balance + 0} WHERE login = "{user_login}"')
        db.commit()
    else:
        #print('Вы проиграли!')
        sql.execute(f'UPDATE users SET cash = {balance - 1000} WHERE login = "{user_login}"')
        db.commit()

def enter():
    for i in sql.execute('SELECT login, cash FROM users'):
        print(i)


def go():
    casino()
    enter()

go()