import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
firm_counter = 0
with open('task7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)

        if profit[name] >= 0:
            prof = prof + profit[name]
            firm_counter += 1
    if firm_counter != 0:
        prof_aver = prof / firm_counter

    dict = {'average_profit' : int(prof_aver)}

    answer = [profit, dict]

with open('task7.json', 'w') as write_js:
    json.dump(answer, write_js)

    js_str = json.dumps(answer)
    print(js_str)