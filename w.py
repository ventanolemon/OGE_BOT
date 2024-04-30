def spis():
    a, n = input('Введите список названий').split(', '), int(input('Введите изменение строки'))
    o = int(input('числ кодировки'))/8
    print(*[a[i] for i in range(len(a)) if len(a[i])*o == (n-2*o)])


def text():
    a = [int(input()) for _ in range(4)]
    return ((a[0]*a[1]*a[2]*(a[3]/8))//1024)


def strok():
    return (int(len(input())*(int(input())/8)))


a = input('Введи номер действ: 1-найти эл в строке, 2-найти объем текста, 3-вес строки: ')
if a == '1':
    spis()
else:
    print(text() if a == '2' else strok())
