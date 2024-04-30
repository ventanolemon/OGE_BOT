# 2 номер ОГЭ
s, s1, ind, flag = input('введи строчку'), ['gammmma'], [], False
a = {input('введи шифровку'): input('введи букву') for _ in range(int(input('введи количество букв')))}
k = list(a.keys())
# k = [input() for _ in range(int(input('vvedi')))]
c, no = {}, {}
for i in k:
    if len(i) not in c:
        c[len(i)] = [i]
    else:
        c[len(i)].append(i)
# print(k, c)
while flag is False:
    for o in list(c.keys()):
        for j in range(len(c[o])):
            if sum(ind) not in no:
                no[sum(ind)] = ['gammmma']
            if len(s1) > 0:
                if c[o][j] == s1[-1]:
                    no[sum(ind)].append(s1[-1])
                    ind.pop(-1)
                    s1.pop(-1)
            # print(c[o][j], s[:sum(ind) + int(o)], ind, o, s1)
            if c[o][j] == s[sum(ind):sum(ind) + int(o)]:
                flag2 = True
                if sum(ind) + len(c[o][j]) in no:
                    flag2 = not(c[o][j] in no[sum(ind) + len(c[o][j])])
                if flag2 == True:
                    if 'gammmma' in s1:
                        s1.remove('gammmma')
                    if len(s1) == 0:
                        no[sum(ind)].append(c[o][j])
                    s1.append(c[o][j])
                    ind.append(o)
            if ''.join(s1) == s:
                flag = True
                break
    if flag is True:
        break
# print(s1)
print(*[a[i] for i in s1], sep='')
