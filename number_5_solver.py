# 5 номер ОГЭ
s = {}
for _ in range(2):
    s1 = input('введи команду').replace(';', '')
    if 'b' in s1 or 'квадрат' in s1:
        s[s1[:s1.index('.')]] = [s1[s1.index('.') + 1:].lower()]
    else:
        s[s1[:s1.index('.')]] = [s1[s1.index('.')+1:-1].lower(), int(s1[-1])]
c = input('введи стр команд').replace(' ', '')
x = int(input('нач зн'))
y = int(input('кон зн'))
su, b = x, 1
while su != y:
    su = x
    b += 1
    for i in c:
        if 'b' not in s[i][0]:
            if 'прибавь' in s[i][0]:
                su += s[i][1]
            elif 'умножь' in s[i][0]:
                su *= s[i][1]
        else:
            if 'умножь' in s[i][0]:
                su *= b
            elif 'прибавь' in s[i][0]:
                su += b
            elif 'раздели' in s[i][0]:
                su /= b
            elif 'вычти' in s[i][0]:
                su -= b
            elif 'квадрат' in s[i][0]:
                su **= 2
print(b)
