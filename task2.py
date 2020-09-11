f = open('task2.txt', encoding='utf-8')


lines = f.readlines()
lines_counter = 0
for line in lines:
    print(line, end='')
    print('Количество слов: ', len(line.split()))
    lines_counter += 1

print('Количество строк: ', lines_counter)

f.close()