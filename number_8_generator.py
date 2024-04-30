# генератор 8 задания
import random


def slovo():
    return [''.join(random.sample('azxswedcvfrtgbnhyujmkilop', random.randint(3, 7))), random.randrange(500, 5000, 100)]


tip = random.choice(('y', 'ili'))
x = slovo()
y = slovo()
obh = x[1] + y[1]
peres = random.randrange(100, min(x[1], y[1]), 100)
zadach, vopr, otv = {}, '', ''
if tip == 'y':
    zadach = {x[0]: x[1], x[0] + ' | ' + y[0]: obh, x[0] + ' & ' + y[0]: peres}
    vopr = 'найдите кол-во страниц по запр: ', y[0]
    otv = obh - x[1] + peres
else:
    tip_1 = random.choice(('and', 'or'))
    if tip_1 == 'and':
        zadach = {x[0]: x[1], x[0] + ' | ' + y[0]: obh, y[0]: y[1]}
        vopr = 'найдите кол-во страниц по запр:', x[0], '&', y[0]
        otv = x[1] + y[1] - peres
    else:
        zadach = {x[0]: x[1], x[0] + ' & ' + y[0]: peres, y[0]: y[1]}
        vopr = 'найдите кол-во страниц по запр:', x[0], '|', y[0]
        otv = x[1] + y[1] - obh
print(vopr, zadach, otv, sep='\n')