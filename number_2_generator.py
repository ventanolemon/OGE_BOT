# генератор 2 номера
import random

import itertools

sl = []
bukv = []
for i in range(1, 5):
    bukv.append([''.join(list(i)) for i in itertools.product('01', repeat=i)])
kol = random.choice([6, 7])
for i in range(kol):
    otv = []
    for i in bukv:
        otv1 = []
        for o in i:
            flag = False
            for j in sl:
                if o[:len(j)] == j or j[:len(o)] == o:
                    flag = True
            if not flag:
                otv1.append(o)
        otv.append(otv1)
    vozm = sum([len(i) for i in otv])
    stroky = 1
    poteri = sum([2 ** i for i in range(stroky + 1, 4)]) + stroky
    while vozm - poteri < kol:
        stroky += 1
        poteri = sum([2 ** i for i in range(stroky + 1, 4)]) + sum([1 for i in range(1, stroky) if len(otv[i])])
        if stroky > 4:
            stroky = 1
    slovo_new = random.choice(otv[stroky])
    kol -= 1
    sl.append(slovo_new)
random.shuffle(sl)
kluchi = random.sample('qwertyuiopasdfg', len(sl))
slovar = {kluchi[i]: sl[i] for i in range(len(sl))}
rashifr = random.sample(list(slovar.keys()), random.randint(3, 6))
kod = ''.join([slovar[i] for i in rashifr])
print(slovar)
print(kod, '\\', rashifr)
