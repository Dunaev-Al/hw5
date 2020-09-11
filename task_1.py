f = open('task1.txt', 'w', encoding='utf-8')
line = str(input('Введите строку в файл \n ')) + '\n'

while line:
    f.write(line)
    line = str(input('Введите строку в файл \n ')) + '\n'
    if line == '\n':
        break

f.close()
