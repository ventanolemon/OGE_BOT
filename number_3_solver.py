# 3 номер ОГЭ
def ne(s):
    return 'не(' in s


def sr(s, x):
    k = ''.join([s[i] for i in range(s.find('x')+1, s.find(')')) if not(s[i].isdigit())])
    b = int(s[s.find(k[-1])+1:s.find(')')])
    return {'<': x < b, '>': x > b, '<=': x <= b, '>=': x >= b, '%': x % b == 0}[k]


def chet(s, x):
    o = s[s.find('x')+1:s.find(')')]
    #print(s, x, o)
    return {'чётное': x % 2 == 0, 'нечётное': x % 2 != 0}[o]


def sotr(s, x):
    if 'чёт' not in s:
        return sr(s, x)
    else:
        return chet(s, x)



def osob(s, x):
    if s.count(')и') == 2:
        an = s.find('и')
        an2 = s[an+1:].find('и') + an + 1
        a, b, c = s[:an], s[an:an2], s[an2:]
        while (int(int(ne(a) ^ (sotr(a, x))) * int(ne(b) ^ (sotr(b, x))) * int(ne(c) ^ (sotr(c, x))))) != 1:
            x += 1
        if 'наименьшее' in n: return x
        while (int(int(ne(a) ^ (sotr(a, x))) * int(ne(b) ^ (sotr(b, x))) * int(ne(c) ^ (sotr(c, x))))) == 1:
            x += 1
            if (int(int(ne(a) ^ (sotr(a, x))) * int(ne(b) ^ (sotr(b, x))) * int(ne(c) ^ (sotr(c, x))))) != 1:
                x += 1
                if (int(int(ne(a) ^ (sotr(a, x))) * int(ne(b) ^ (sotr(b, x))) * int(ne(c) ^ (sotr(c, x))))) != 1: x -= 1
        return x - 1
    elif 'или' in s:
        an = n.find('и')
        a, b = n[:an], n[an + 1:]
        while (int(int(ne(a) ^ (sotr(a, x))) + int(ne(b) ^ (sotr(b, x))))) == 1: x += 1
        return x
    else:
        x = 10
        an = s.find(')и')
        a, b = s[:an+1].replace('перваяцифра', 'x').replace('чётная', 'чётное'), s[an + 1:]
        f = str(x)
        while int(int(ne(a) ^ (chet(a, int(f[0])))) * int(ne(b) ^ (x % 3 == 0))) != 1:
            x += 1
            f = str(x)
        if 'наименьшее' in s:
            return x
        else:
            x2 = x
            while len(f) == 2:
                x += 1; f = str(x)
                if int(int(ne(a) ^ (chet(a, int(f[0])))) * int(ne(b) ^ (x % 3 == 0))) == 1 and len(f) == 2:
                    x2 = x
        return x2


n, x = input('введите пример,а после него наибольшее/наименьшее(при необх напиш10000 сл)\n').lower().replace(' ', '')\
    .replace('число', 'x').replace('кратно', '%'), 1
if n.count('или') == 0 and n.count('(') == 2 and not'делится' in n and not'цифра' in n:
    an = n.find('и')
    a, b = n[:an], n[an+1:]
    while (int(int(ne(a) ^ (sotr(a, x))) * int(ne(b) ^ (sotr(b, x))))) != 1:
        x += 1
    if 'наименьшее' in n:
        print(x)
    else:
        while (int(int(ne(a) ^ (sotr(a, x))) * int(ne(b) ^ (sotr(b, x))))) == 1:
            x += 1
            if (int(int(ne(a) ^ (sotr(a, x))) * int(ne(b) ^ (sotr(b, x))))) != 1 and 'чёт' in n:
                x += 1
                if (int(int(ne(a) ^ (sotr(a, x))) * int(ne(b) ^ (sotr(b, x))))) != 1: x -= 1
        print(x-1)
else: print(osob(n, x))
#((ne(a) ^ (chet(a, x[0]))) and (ne(b) ^ (x % 3 == 0)))