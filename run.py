import random

file = open('randomData.txt', 'w')

rows = input('How many rows to generate: ')
columns = input('How many columns to generate: ')
lint = input('Lower interval: ')
hint = input('Higher interval: ')

for r in range(int(rows)):
    for c in range(int(columns)):
        file.write('%s ' % random.randint(int(lint), int(hint)))
    file.write('\n')

print('Data is saved to "randomData.txt"')
