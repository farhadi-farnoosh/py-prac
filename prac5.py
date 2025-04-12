#for count the number of each proper noun
# word = {}
# text = input().split('. ')
# text[-1] = text[-1][:-1]

# for i in range(len(text)):
#     text[i] = text[i].split(' ')
#     del(text[i][0])
#     text[i] = ' '.join(text[i])

# text = ' '.join(text)
# text = text.split()

# for i in range(len(text)):
#     if text[i].endswith(','):
#         text[i] = text[i][:-1]

# for i in text:
#     if i.istitle():
#         word[i] = 1

# for i in word:
#     word[i] = text.count(i)

# if word == {}:
#     print(None)
# else:
#      for key, value in word.items(): print(value, ':', key, sep='')

word = []
text = input().split('. ')
text[-1] = text[-1][:-1]

for i in range(len(text)):
    text[i] = text[i][0].lower() + text[i][1:]

text = ' '.join(text)
text = text.split()

for i in range(len(text)):
    if text[i].endswith(','):
        text[i] = text[i][:-1]
    if text[i].istitle():
        word.append([i+1, text[i]])

if word == []:
    print(None)
else:
    for i in range(len(word)):
        print(f'{word[i][0]}:{word[i][1]}')