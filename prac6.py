
persian = []
english = []
french = []
german = []
translate = ''

for _ in range(int(input())):
    x = input().split()
    persian.append(x[0])
    english.append(x[1])
    french.append(x[2])
    german.append(x[3])

sentence = input().split()

for i in sentence:
    if i in english:
        x = english.index(i)
        translate = translate + persian[x] + ' '
    elif i in french:
        x = french.index(i)
        translate = translate + french[x] + ' '
    elif i in german:
        x = german.index(i)
        translate = translate + german[x] + ' '
    else:
        translate = translate + i + ' '

print(translate[:-1])

