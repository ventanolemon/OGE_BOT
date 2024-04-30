# 10 номер ОГЭ
def chisla():
    n, s = input('введи минимальное или максимальное значение нужно\n').replace(' ', ''), []
    for i in range(int(input('введи количество чисел\n'))):
        s.append(int(input('введи число\n'), int(input('введи основание системы счисления\n'))))
    return {'минимальное': min(s), 'максимальное': max(s)}[n]


def perev():
    return int(input('введи число\n'), int(input('введи основание системы счисления\n')))


def schet():
    n, i, oce, k, dey = int(input('введи количество чисел\n')), int(input('введи нужную сс\n')), [], \
                       input('введи минимальное или максимальное нужно\n'), \
                       input('введи сумм  каких цифр найти или просто сумм, если сумма всех цифр нужна\n')
    for _ in range(n):
        a, oc = int(input('введи число в 10 сс\n')), []
        while a >= i:
            oc.append(a % i)
            a //= i
        oc.append(a)
        oce.append(oc[::-1])
    if 'сумм' in dey:
        otv = []
        for o in range(n):
            otv.append(sum(oce[o]))
    else:
        otv = []
        for o in range(n):
            otv.append(oce[o].count(int(dey)) * int(dey))
    return {'минимальное': min(otv), 'максимальное': max(otv)}[k]

a = input('введи номер, где 1 - поиск минимального/максимального, 2 - перевод числа из одной сс в другую, '
          '3 - поиск сумм значений\n')
if a == '1':
    print(chisla())
elif a == '2':
    print(perev())
else:
    print(schet())
