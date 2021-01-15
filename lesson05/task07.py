"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна
содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли
ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить
ее в словарь (со значением убытков).

Пример списка:
[{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json


rawfile = None
common_list, firms_list, avg_profit = [], {}, {}
name, firm_profit = '', []
count = 0

with open('org.txt', 'r') as file:
    rawfile = file.readlines()

for line in rawfile:
    name = line.split()[0]
    firms_list[name] = int(line.split()[2]) - int(line.split()[3])

pos_income = [_ for _ in firms_list.values() if _ > 0]
avg_profit['average_profit'] = int(sum(pos_income) / len(pos_income))

common_list.append(firms_list)
common_list.append(avg_profit)

with open('org.json', 'w') as json_file:
    json_file.write(json.dumps(common_list))
