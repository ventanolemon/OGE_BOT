
# 8 номер ОГЭ
def y():
    s = {}
    for i in range(3):
        c = input()
        if '|' in c:
            c1 = 'or'
        elif '&' in c:
            c1 = 'and'
        else:
            c1 = 'x'
        s[c1] = int(c[c.index('\t'):].replace('\t', ''))
    return s['or'] - s['x'] + s['and']


def ili():
    s = {'x_y': []}
    for i in range(3):
        c = input()
        if '|' in c:
            s['or'] = int(c[c.index('\t'):].replace('\t', ''))
        elif '&' in c:
            s['and'] = int(c[c.index('\t'):].replace('\t', ''))
        else:
            s['x_y'].append(int(c[c.index('\t'):].replace('\t', '')))
    if 'and' in list(s.keys()):
        return sum(s['x_y']) - s['and']
    else:
        return sum(s['x_y']) - s['or']


vib = input('введи "y" если нужно найти кол одного запроса, "или" есл нужно найти или/и 2 запросов\n').replace('у', 'y')
if vib == 'y':
    print(y())
else:
    print(ili())