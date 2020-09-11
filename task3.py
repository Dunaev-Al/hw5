f = open('task3.txt', encoding='utf-8')

lines = f.readlines()
poor = []
workers = 0
sum = 0
for line in lines:
    arr = line.split()
    if int(arr[1]) < 20000:
        print('Доход меньше 20 тысяч у ', str(arr[0]) + 'a')
    sum += int(arr[1])
    workers += 1

middle_wage = sum / workers
print('Средний заработок равен: ', int(middle_wage))
f.close()