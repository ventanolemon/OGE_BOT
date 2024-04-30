def g_1():
    sl = {input('значение:\n').replace('.', ''): input('буква:\n') for _ in range(7)}
    n = input('Введи текст задачи\n')
    f = n.find('файлу') + 6
    doth = n.find('.')
    file = n[f:doth]
    form = n[doth + 1:n[doth:].find(',')+doth]
    f = n.find('сервере') + 8
    n = n[f:]
    doth = n.find('.')
    serv = n[:doth]
    okon = n[doth + 1:n[doth:].find(',')+doth]
    n = n[doth + 1:]
    prot = n[n.find('протоколу') + 10:n.find('.')]
    return ''.join([sl[prot], sl['://'], sl[serv], sl[okon], sl['/'], sl[file], sl[form]])


def g_2():
    import itertools
    sl, c = {input('значение:\n'): input('буква:\n') for _ in range(4)}, []
    s = list(sl.keys())
    g = [list(g) for g in itertools.permutations(s, 4)]
    for i in range(len(g)):
        if g[i][0][0] == '.' or g[i][-1][-1] == '.':
            c.append(g[i])
        d = (''.join(g[i])).split('.')
        for o in range(len(d)):
            if g[i] not in c:
                if int(d[o]) > 255 and d[o] not in c:
                    c.append(g[i])
    for j in range(len(c)):
        g.remove(c[j])
    return ''.join([sl[g[0][0]], sl[g[0][1]], sl[g[0][2]], sl[g[0][3]]])


def g_3():
    pass


gr = input('введи 1, если файл не перем, иначе 3, если ip, то введи 2')
print(g_1() if gr == '1' else g_2() if gr == '2' else g_3())
