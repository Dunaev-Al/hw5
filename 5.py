f = open('task5.txt', encoding='utf-8')
sum = 0
line = f.readline()
arr = line.split()
for el in arr:
    sum += int(el)
print(sum)
f.close()
