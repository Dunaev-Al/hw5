f = open('task4.txt', encoding='utf-8')
f_new = open('task4_new.txt', 'w', encoding='utf-8')
rus_arr = ['Один', 'Два', 'Три', 'Четыре']
index = 0

lines = f.readlines()
for line in lines:
    arr = line.split()
    new_str = rus_arr[index] + ' ' + arr[1] + ' ' + arr[2] + '\n'
    index += 1
    f_new.write(new_str)

f.close()
f_new.close()

