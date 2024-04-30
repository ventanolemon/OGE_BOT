# генератор 10 задания
import random


chisl = random.sample(range(10, 100), 3)
print(chisl)
otv = max(chisl)
chisl = ['в 2ичной:' + bin(chisl[0])[2:], 'в 8ичной:' + oct(chisl[0])[2:], 'в 16ичной:' + hex(chisl[0])[2:]]
print('найдите максимальное в 10ичной:', chisl, '\\', otv)
