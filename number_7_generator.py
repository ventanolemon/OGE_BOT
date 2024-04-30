# генератор 7 номера
import random


def rtxt():
    return ''.join(random.sample('qazxswedcvfrtgbnhyujmikolp', random.randint(3, 6)))


format = ['.bmp', '.txt', '.gif', '.htm', '.xls', '.xml', '.doc', '.pdf', '.jpg', '.net', '.lib', '.pas']
serv = ['.org', '.com', '.ru', '.kz', '.net', '.info', '.рф']
protocol = ['http', 'ftp', 'https', 'ftp']
file = [random.choice(protocol), '://', rtxt() + random.choice(serv), '/', rtxt() + random.choice(format)]
file_mixed = file
print(file)
random.shuffle(file_mixed)
kluchi = random.sample('qwertyuiopasdfg', len(file))
slovar = {kluchi[i]: file_mixed[i] for i in range(len(file_mixed))}
print(slovar)
