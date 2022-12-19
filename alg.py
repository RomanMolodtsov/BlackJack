import random, time

def first():
    global x
    global result
    global tuz
    x = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    if x == 11:
        tuz += 1
    result += x
    print(x)
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


tuz = 0
result = 0
tuz_crup = 0
res_crup = 0
number = 0
first()
first()
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
        else:
            print(f'Я набрал {res_crup}, это перебор!')
            number = 1
            break
if result > res_crup and result < 22:
    print('Ты выиграл!')
    number = 1
elif result < res_crup and res_crup < 22:
    print('Ты проиграл!')
    number = 0
elif result == res_crup and result < 22:
    print('Ничья!')

