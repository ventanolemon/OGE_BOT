#  генератор 6 задания
def sr(chisl):
    if chisl[2] == '<':
        return chisl[0] < chisl[1]
    elif chisl[2] == '<=':
        return chisl[0] <= chisl[1]
    elif chisl[2] == '>':
        return chisl[0] > chisl[1]
    elif chisl[2] == '>=':
        return chisl[0] > chisl[1]

def sopost(znach):
    return sr(znach[0]) * sr(znach[1]) if souz == 'and' else sr(znach[0]) + sr(znach[1])

import random


chisloN = [random.randint(1, 100), random.choice(('<', '<=', '>', '>='))]  # задаем число с кот будем ср и знак алг-лог
chisloT = [random.randint(1, 100), random.choice(('<', '<=', '>', '>='))]
vivod = not(random.choice([True, False]))  # выбираем выводы NO или YES будем считать
count, souz = 0, random.choice(('and', 'or'))
nabori = []
for i in range(9):
    nab = [random.randint(-25, 100), random.randint(-25, 100)]  # создаем пару чисел
    count += int(sopost([[nab[0], *chisloN], [nab[1], *chisloT]]) != vivod) # передаем список списков с числом набораи и соот ему числ N, T
    nabori.append(nab)
print(f'найдите сколько раз будет выведен {"YES" if vivod else "NO"}\n'
      f'данной программой: N {chisloN[1]} {chisloN[0]} {souz} T {chisloT[1]} {chisloT[0]} \n'
      f'и данном наборе знач {nabori}', count)
