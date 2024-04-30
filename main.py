'''
guys = {}
for _ in range(int(input())):
    guy = input().split()
    if guy[-1] not in guys:
        guys[guy[-1]] = [[guy[0], int(guy[1])]]
    else:
        guys_special = {int(guy[1]): guy[0]}
        for i in guys[guy[-1]]:
            if i[1] not in guys_special:
                guys_special[int(i[1])] = [i[0]]
            else:
                guys_special[int(i[1])].append(i[0])
                guys_special[int(i[1])].sort()
        guys[guy[-1]] = guys_special
for _ in range(int(input())):
    c = guys.get(input())
    if type(c) is dict:
        k, otv = list(c.keys()), ''
        k.sort()
        for i in k:
            if type(c[i]) is list:
                otv += c[i][0] + ' ' + str(i) + ' '
            else:
                otv += c[i] + ' ' + str(i) + ' '
        print(otv)
    elif type(c) is list:
        c = [' '.join([str(o) for o in i]) for i in c]
        print(*c)
    gfew
['i', 'y', 'r', 'o', 'g']
'''

while True:
    modul = input()
    if modul == '1':
        import number_1_solver
    elif modul == '1_g':
        import number_1_generator
    elif modul == '2':
        import number_2_solver
    elif modul == '2_g':
        import number_2_generator
    elif modul == '3':
        import number_3_solver
    elif modul == '3_g':
        import number_3_generator
    elif modul == '5':
        import number_5_solver
    elif modul == '5_g':
        import number_5_generator
    elif modul == '6':
        import number_6_solver
    elif modul == '6_g':
        import number_6_generator
    elif modul == '7':
        import number_7_solver
    elif modul == '7_g':
        import number_7_generator
    elif modul == '8':
        import number_8_solver
    elif modul == '8_g':
        import number_8_generator
    elif modul == '10':
        import number_10_solver
    elif modul == '10_g':
        import number_10_generator

