# 6 номер ОГЭ
def deyst(k, zn):
    if '<' in k:
        return zn < int(k[k.index('<') + 1])
    elif '>' in k:
        return zn > int(k[k.index('>') + 1])
    elif '*' in k:
        return zn * int(b[0])
    elif '//' in k:
        return zn // int(k[k.index('//') + 2])

def sr(c, zn):
    if c == 'or':
        return deyst(a, zn[0]) or deyst(b, zn[1])
    elif c == 'and':
        return deyst(a, zn[0]) and deyst(b, zn[1])
    elif c == '<=':
        return zn[0] <= deyst(b, zn[1])
    elif c == '>=':
        return zn[0] >= deyst(b, zn[1])
    elif c == '==':
        return deyst(a, zn[0]) == zn[1]


st = input('введи строку с началом усл оператора\n')
zap = input('введи строку со значениями\n').split('; ')
otv, count = bool(int(input('введи 1 если True или 0 если False нужно считать\n'))), 0
zap_kor = []
for i in range(len(zap)):
    if '\u2009' in zap[i]:
        zap[i] = zap[i].replace('\u2009', ' ')
    zap_kor.append(zap[i].split(', '))
for i in range(len(zap_kor)):
    for o in range(len(zap_kor[i])):
        if '\u2009' in zap_kor[i][o]:
            zap_kor[i][o] = zap_kor[i][o].replace('\u2009', ' ')
            zap_kor[i][o] = zap_kor[i][o].split(', ')
        zap_kor[i][o] = int(zap_kor[i][o].replace('(', '').replace(')', '').replace('–', '-').replace('.', '')
                            .replace('−', '-').replace('—', '-'))
st = st[st.index('s'):st.index(':')]
if 'or' in st or 'and' in st:
    if 'or' in st:
        a = st[:st.index('or')].replace(' ', '')
        c = 'or'
        b = st[st.index('or') + 2:].replace(' ', '')
    elif' and' in st:
        a = st[:st.index('and')].replace(' ', '')
        c = 'and'
        b = st[st.index('and') + 2:].replace(' ', '')
else:
    if '==' in st:
        a = st[:st.index('=')].replace(' ', '')
        c = '=='
    elif '=' in st:
        a = st[:st.index('s')].replace(' ', '')
        c = st[st.index('s') + 1:st.index('2')]
        b = st[st.index('2'):]
# print('=' in st, st)
for j in range(len(zap_kor)):
    if sr(c, zap_kor[j]) == otv:
        count += 1
print(count)
