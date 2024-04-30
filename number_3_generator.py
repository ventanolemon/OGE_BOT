# генератор 3 задания
import random


def vib(d, gr, chetn):
    otr = random.choice([True, False])
    if chetn:
        viv = f'(x {"не" if chislo % 2 != 0 else ""}четное)'
    elif gr != otr:
        znak = random.choice(['<', '<='])
        if not gr and znak == '<':
            d -= 1
            znak = '<='
        elif not gr:
            d -= 1
            znak = '<'
        viv = f'{"НЕ" if otr else ""}(x {znak} {d if znak == "<=" else d + 1})'
    else:
        znak = random.choice(['>', '>='])
        if gr and znak == '>':
            znak = '>='
            d += 1
        elif gr:
            znak = '>'
            d += 1
        viv = f'{"НЕ" if otr else ""}(x {znak} {d if znak == ">=" else d - 1})'
    return viv


chislo = random.randint(1, 100)
gran = random.choice([True, False])  # True - верхн грань, False - нижняя
chetn = random.choice([True, False])  # True - одно из усл на четн числа
if gran:
    diap = [random.randint(1, chislo - 1), chislo + (chetn * (chislo % 2))]
    otv1 = vib(diap[0], False, chetn)
    otv2 = vib(diap[1], True, False)
else:
    diap = [chislo - (chetn * (chislo % 2)), random.randint(chislo + 1, 102)]
    otv1 = vib(diap[0], False, False)
    otv2 = vib(diap[1], True, chetn)
print(chislo, gran, chetn, '\\', 'макс знач x в диапазоне' if gran else 'мин знач x в диапозоне', otv1 + ' И ' + otv2)
