# 1 номер ОГЭ
def spis():
    nazv, izm = input('Введите список названий').split(', '), int(input('Введите изменение строки'))
    codir = int(input('числ кодировки'))/8
    print(nazv)
    print(*[nazv[i] for i in range(len(nazv)) if len(nazv[i]) * codir == izm - 2 * codir])


def text():
    a = [int(input()) for _ in range(4)]
    return ((a[0]*a[1]*a[2]*(a[3]/8))//1024)


def strok():
    return (int(len(input())*(int(input())/8)))


tip = input('Введи номер действ: 1-найти эл в строке, 2-найти объем текста, 3-вес строки: ')
if tip == '1':
    spis()
else:
    print(text() if tip == '2' else strok())
#  - 2 * codir