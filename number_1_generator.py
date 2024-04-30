# генератор 1 номера
from random import *


bukv = 'qwertyuiopasdfghjklzxcvbnm'
cen = choice([1, 2, 4, 6, 8])
kol = randint(6, 10)
dlin = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
strok = []
for _ in range(kol):
    dlin1 = choice(dlin)
    strok.append(''.join([choice(bukv) for _ in range(dlin1)]))
    dlin.remove(dlin1)
otv = choice(strok)
print(cen, kol, strok, otv)
print(f'Каждый символ кодируется {8 * cen} битами. Был текст: {", ".join(strok)}. \n'      f'Вычеркнули слово, после чего вес предложения уменьшился на {(len(otv) + 2) * cen} байт, какое слово вычеркнули?')
