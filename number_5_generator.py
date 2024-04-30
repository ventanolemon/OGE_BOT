# генератор 5 задания
import random


deyst = random.choice(('прибавь', 'возведи в квадрат', 'умножь на', 'вычти', 'прибавь', 'прибавь'))
if deyst == 'прибавь':
    deyst1 = random.randint(1, 10)
    deyst_b = 'умножь на b'
    nom_b = random.randint(0, 4)
    b = random.randint(1, 12)
    com = '1' * nom_b + '2' + '1' * (4 - nom_b)
    nach = konch = random.randint(1, 10)
    for i in com:
        if i == '1':
            konch += deyst1
        else:
            konch *= b
elif deyst == 'возведи в квадрат':
    deyst1 = ''
    deyst_b = 'прибавь b'
    nom_deyst = random.sample([i for i in range(0, 4)], 2)
    b = random.randint(1, 5)
    com = ''.join([{0: '2', 1: '1'}[int(i in nom_deyst)] for i in range(5)])
    nach = konch = random.randint(2, 4)
    for i in com:
        if i == '1':
            konch **= 2
        else:
            konch += b
elif deyst == 'умножь на':
    deyst1 = random.randint(1, 10)
    deyst_b = 'прибавь b'
    nom_b = random.sample([i for i in range(0, 5)], 3)
    b = random.randint(1, 15)
    com = ''.join([{0: '1', 1: '2'}[int(i in nom_b)] for i in range(5)])
    nach = konch = random.randint(1, 30)
    for i in com:
        if i == '1':
            konch *= deyst1
        else:
            konch += b
elif deyst == 'вычти':
    deyst = 'умножь на'
    deyst1 = random.randint(1, 6)
    deyst_b = 'вычти b'
    nom_b = random.sample([i for i in range(0, 5)], 3)
    b = random.randint(1, 5)
    com = ''.join([{0: '1', 1: '2'}[int(i in nom_b)] for i in range(5)])
    nach = konch = random.randint(b * 3 + 1, 30)
    for i in com:
        if i == '1':
            konch *= deyst1
        else:
            konch -= b
print(f'1. {deyst} {deyst1} \n2. {deyst_b} \nалгоритм: {com}\nпереводит {nach} в {konch}, найдите b', '\\', b)
