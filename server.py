from flask import Flask

app = Flask(__name__)


@app.route('/')

from random import *


import random

tok = telebot.TeleBot('5662277208:AAGFv66IfUyCKvQPez0CQp4S2lOoVP8O00E')


@tok.message_handler(commands=['dat'])
def sandle(message):
    print(type(message))
    a = []
    for _ in range(3):
        a.append(message.text)
        tok.send_message(message.chat.id, 'след')
    tok.send_message(message.chat.id, a)


@tok.message_handler(commands=['1_g'])
def generator_1(message):
    bukv = 'qwertyuiopasdfghjklzxcvbnm'
    cen = choice([1, 2, 4, 6, 8])
    kol = randint(6, 10)
    dlin = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    strok = []
    for _ in range(kol):
        dlin1 = choice(dlin)
        strok.append(''.join([choice(bukv) for _ in range(dlin1)]))
        dlin.remove(dlin1)
    otv = choice(strok)
    print(cen, kol, strok, otv)
    print(f'Каждый символ кодируется {8 * cen} битами. Был текст: {", ".join(strok)}. \n'      
          f'Вычеркнули слово, после чего вес предложения уменьшился на {(len(otv) + 2) * cen} байт, '
          f'какое слово вычеркнули?')
    tok.send_message(message.chat.id, f'Каждый символ кодируется {8 * cen} битами. Был текст: {", ".join(strok)}. \n'
                                      f'Вычеркнули слово, после чего вес предложения уменьшился на {(len(otv) + 2) * cen} байт, '
                                      f'какое слово вычеркнули?')
    otvet = f'Ответ: ||{otv}||'
    tok.send_message(message.chat.id, otvet, parse_mode='MarkdownV2')


@tok.message_handler(commands=['2_g'])
def generator_2(message):
    import itertools

    sl = []
    bukv = []
    for i in range(1, 5):
        bukv.append([''.join(list(i)) for i in itertools.product('01', repeat=i)])
    kol = random.choice([6, 7])
    for i in range(kol):
        otv = []
        for i in bukv:
            otv1 = []
            for o in i:
                flag = False
                for j in sl:
                    if o[:len(j)] == j or j[:len(o)] == o:
                        flag = True
                if not flag:
                    otv1.append(o)
            otv.append(otv1)
        vozm = sum([len(i) for i in otv])
        stroky = 1
        poteri = sum([2 ** i for i in range(stroky + 1, 4)]) + stroky
        while vozm - poteri < kol:
            stroky += 1
            poteri = sum([2 ** i for i in range(stroky + 1, 4)]) + sum([1 for i in range(1, stroky) if len(otv[i])])
            if stroky > 4:
                stroky = 1
        slovo_new = random.choice(otv[stroky])
        kol -= 1
        sl.append(slovo_new)
    random.shuffle(sl)
    kluchi = random.sample('qwertyuiopasdfg', len(sl))
    slovar = {kluchi[i]: sl[i] for i in range(len(sl))}
    rashifr = random.sample(list(slovar.keys()), random.randint(3, 6))
    kod = ''.join([slovar[i] for i in rashifr])
    print(slovar)
    print(kod, '\\', rashifr)
    tok.send_message(message.chat.id, f'расшифруйте слово {str(kod)}, если:\n' +
                     '\n'.join([i + '\) ' + slovar[i] for i in slovar.keys()]), parse_mode='MarkdownV2')
    otvet = f'Ответ: ||{"".join(rashifr)}||'
    tok.send_message(message.chat.id, otvet, parse_mode='MarkdownV2')


@tok.message_handler(commands=['3_g'])
def generator_3(message):
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
    print(chislo, gran, chetn, '\\', 'макс знач x в диапазоне' if gran else 'мин знач x в диапозоне',
          otv1 + ' И ' + otv2)
    tok.send_message(message.chat.id, ''.join(['макс знач x в диапазоне: \n' if gran else 'мин знач x в диапозоне: \n',
                                               str(otv1) + ' И ' + str(otv2)]))
    otvet = f'Ответ: ||{chislo}||'
    tok.send_message(message.chat.id, otvet, parse_mode='MarkdownV2')


@tok.message_handler(commands=['5_g'])
def generator_5(message):
    deyst = random.choice(('прибавь', 'возведи в квадрат', 'умножь на', 'вычти', 'прибавь', 'прибавь'))
    if deyst == 'прибавь':
        deyst1 = random.randint(1, 10)
        deyst_b = 'умножь на b'
        nom_b = random.randint(0, 4)
        b = random.randint(1, 12)
        com = '1' * nom_b + '2' + '1' * (4 - nom_b)
        nach = konch = random.randint(1, 10)
        for i in com:
            if i == '1':
                konch += deyst1
            else:
                konch *= b
    elif deyst == 'возведи в квадрат':
        deyst1 = ''
        deyst_b = 'прибавь b'
        nom_deyst = random.sample([i for i in range(0, 4)], 2)
        b = random.randint(1, 5)
        com = ''.join([{0: '2', 1: '1'}[int(i in nom_deyst)] for i in range(5)])
        nach = konch = random.randint(2, 4)
        for i in com:
            if i == '1':
                konch **= 2
            else:
                konch += b
    elif deyst == 'умножь на':
        deyst1 = random.randint(1, 10)
        deyst_b = 'прибавь b'
        nom_b = random.sample([i for i in range(0, 5)], 3)
        b = random.randint(1, 15)
        com = ''.join([{0: '1', 1: '2'}[int(i in nom_b)] for i in range(5)])
        nach = konch = random.randint(1, 30)
        for i in com:
            if i == '1':
                konch *= deyst1
            else:
                konch += b
    elif deyst == 'вычти':
        deyst = 'умножь на'
        deyst1 = random.randint(1, 6)
        deyst_b = 'вычти b'
        nom_b = random.sample([i for i in range(0, 5)], 3)
        b = random.randint(1, 5)
        com = ''.join([{0: '1', 1: '2'}[int(i in nom_b)] for i in range(5)])
        nach = konch = random.randint(b * 3 + 1, 30)
        for i in com:
            if i == '1':
                konch *= deyst1
            else:
                konch -= b
    print(f'1. {deyst} {deyst1} \n2. {deyst_b} \nалгоритм: {com}\nпереводит {nach} в {konch}, найдите b', '\\', b)
    tok.send_message(message.chat.id, str(f'1. {deyst} {deyst1} \n2. {deyst_b} \nалгоритм: {com}\nпереводит {nach} в {konch}, найдите b'))
    otvet = f'Ответ: ||{b}||'
    tok.send_message(message.chat.id, otvet, parse_mode='MarkdownV2')


@tok.message_handler(commands=['6_g'])
def generator_6(message):
    def sr(chisl):
        if chisl[2] == '<':
            return chisl[0] < chisl[1]
        elif chisl[2] == '<=':
            return chisl[0] <= chisl[1]
        elif chisl[2] == '>':
            return chisl[0] > chisl[1]
        elif chisl[2] == '>=':
            return chisl[0] > chisl[1]

    def sopost(znach):
        return sr(znach[0]) * sr(znach[1]) if souz == 'and' else sr(znach[0]) + sr(znach[1])


    chisloN = [random.randint(1, 100),
               random.choice(('<', '<=', '>', '>='))]  # задаем число с кот будем ср и знак алг-лог
    chisloT = [random.randint(1, 100), random.choice(('<', '<=', '>', '>='))]
    vivod = not (random.choice([True, False]))  # выбираем выводы NO или YES будем считать
    count, souz = 0, random.choice(('and', 'or'))
    nabori = []
    for i in range(9):
        nab = [random.randint(-25, 100), random.randint(-25, 100)]  # создаем пару чисел
        count += int(sopost([[nab[0], *chisloN], [nab[1],
                                                  *chisloT]]) != vivod)  # передаем список списков с числом набораи и соот ему числ N, T
        nabori.append(nab)
    print(f'найдите сколько раз будет выведен {"YES" if vivod else "NO"}({count})\n'
          f'данной программой: N {chisloN[1]} {chisloN[0]} {souz} T {chisloT[1]} {chisloT[0]} \n'
          f'и данном наборе знач {nabori}', count)
    tok.send_message(message.chat.id, f'найдите сколько раз будет выведен {"YES" if vivod else "NO"}\n'
          f'данной программой: N {chisloN[1]} {chisloN[0]} {souz} T {chisloT[1]} {chisloT[0]} \n'
          f'и данном наборе значений {", ".join(str(i) for i in nabori)}')
    otvet = f'Ответ: ||{count}||'
    tok.send_message(message.chat.id, otvet, parse_mode='MarkdownV2')


@tok.message_handler(commands=['7_g'])
def generator_7(message):
    def rtxt():
        return ''.join(random.sample('qazxswedcvfrtgbnhyujmikolp', random.randint(3, 6)))

    format = ['.bmp', '.txt', '.gif', '.htm', '.xls', '.xml', '.doc', '.pdf', '.jpg', '.net', '.lib', '.pas']
    serv = ['.org', '.com', '.ru', '.kz', '.net', '.info', '.рф']
    protocol = ['http', 'ftp', 'https', 'ftp']
    file = [random.choice(protocol), '://', rtxt() + random.choice(serv), '/', rtxt() + random.choice(format)]
    file_mixed = file.copy()
    print(file)
    random.shuffle(file_mixed)
    kluchi = random.sample('qwertyuiopasdfg', len(file))
    slovar = {kluchi[i]: file_mixed[i] for i in range(len(file_mixed))}
    print(slovar, str(file))
    tok.send_message(message.chat.id, 'соберите название ссылки в интеренете' + ', если \n'
                     + '\n'.join([i + ') ' + slovar[i] for i in sorted(slovar.keys())]))
    otvet = f'Ответ: ||{"".join(file)} ||'
    print(otvet)
    tok.send_message(message.chat.id, otvet.replace('.', '\.'), parse_mode='MarkdownV2')


@tok.message_handler(commands=['8_g'])
def generator_8(message):
    def slovo():
        return [''.join(random.sample('azxswedcvfrtgbnhyujmkilop', random.randint(3, 7))),
                random.randrange(500, 5000, 100)]

    tip = random.choice(('y', 'ili'))
    x = slovo()
    y = slovo()
    obh = x[1] + y[1]
    peres = random.randrange(100, min(x[1], y[1]), 100)
    zadach, vopr, otv = {}, '', ''
    if tip == 'y':
        zadach = {x[0]: x[1], x[0] + ' | ' + y[0]: obh, x[0] + ' & ' + y[0]: peres}
        vopr = 'найдите кол-во страниц по запросу: ', y[0]
        otv = obh - x[1] + peres
    else:
        tip_1 = random.choice(('and', 'or'))
        if tip_1 == 'and':
            zadach = {x[0]: x[1], x[0] + ' | ' + y[0]: obh, y[0]: y[1]}
            vopr = 'найдите кол-во страниц по запросу:', x[0], '&', y[0]
            otv = x[1] + y[1] - peres
        else:
            zadach = {x[0]: x[1], x[0] + ' & ' + y[0]: peres, y[0]: y[1]}
            vopr = 'найдите кол-во страниц по запросу:', x[0], '|', y[0]
            otv = x[1] + y[1] - obh
    print(vopr, zadach, otv, sep='\n')
    print(vopr)
    tok.send_message(message.chat.id, str(' '.join(vopr)) + '\n' + '\n'.join(i + ': ' + str(zadach[i]) for i in zadach.keys()))
    otvet = f'Ответ: ||{otv}||'
    tok.send_message(message.chat.id, otvet, parse_mode='MarkdownV2')


@app.route('/gn_10')
def generator_10(message):
    chisl = random.sample(range(10, 100), 3)
    print(chisl)
    otv = max(chisl)
    chisl = ['в 2ичной:' + bin(chisl[0])[2:], 'в 8ичной:' + oct(chisl[1])[2:], 'в 16ичной:' + hex(chisl[2])[2:]]
    print('найдите максимальное в 10ичной:', chisl, '\\', otv)
    tok.send_message(message.chat.id, 'найдите максимальное в 10ичной среди данных 3 чисел: ' + '\n' + '\n'.join(chisl))
    otvet = f'Ответ: ||{otv}||'
    return """"""

'''
@app.route('/index')
def sandler(message):
    tok.send_message(message.chat.id, 'Пожалуйста, выберите одну из доступных команд')
'''
@app.route('/index')
def index():
    return "Привет, Яндекс!"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')