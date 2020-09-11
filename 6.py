def symbols(string):
    l = len(string)
    arr = []
    i = 0
    while i < l:
        s_int = ''
        a = string[i]
        while '0' <= a <= '9':
            s_int += a
            i += 1
            if i < l:
                a = string[i]
            else:
                break
        i += 1
        if s_int != '':
            arr.append(int(s_int))
    return arr[0]

arr = []

f = open('task6.txt', encoding='utf-8')
lines = f.readlines()
sum = 0
arr_new = []
dict = {}

for line in lines:
    new_str = str(line)
    arr = new_str.split()
    arr_new.append(arr[0])
    for i in range(1, 4):
        if arr[i] != '—':
            number = symbols(arr[i])
            sum += number
    arr_new.append(sum)
    sum = 0


dict = {arr_new[0] : arr_new[1], arr_new[2] : arr_new[3], arr_new[4] : arr_new[5]}
print(dict)