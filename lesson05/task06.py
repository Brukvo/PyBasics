"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка
описывает учебный предмет и наличие лекционных, практических и лабораторных
занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий
по нему. Вывести словарь на экран.
Примеры строк файла:

Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:

{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def parsenums(numbers):
    """
    Функция принимает список целых чисел, как отрицательных, так и
    положительных, в строковом представлении и возвращает их в виде целых чисел.
    :param numbers: список чисел в их строковом предствалении (напр., ['-3', 2])
    :return: список целых чисел (напр., [-3, 2])
    """
    parsed_numbers = []
    temp_num = None
    for number in numbers:
        if number[0] == '-':
            temp_num = number[1:]
            if temp_num.isnumeric():
                temp_num = int(temp_num)
                parsed_numbers.append(temp_num - (temp_num * 2))
                continue
            else:
                parsed_numbers.append(0)
        if number.isnumeric():
            parsed_numbers.append(int(number))
        else:
            parsed_numbers.append(0)
    return parsed_numbers



raw_lines = None
# subjects_lst, subj_splitted, subj_quan = [], [], []
types = ['(л)', '(пр)', '(лаб)']
subjects = {}

with open('subjects.txt', 'r') as file:
    raw_lines = file.readlines()

for line in raw_lines:
    subjects[(line.split()[0][:-1])] = line.split()[1:]

for subject in subjects.keys():
    _ = []
    for item in subjects[subject]:
        for worktype in types:
            if worktype in item:
                _.append(item.replace(worktype, ''))
                break
            elif item == '-':
                _.append('0')
                break
    subjects[subject] = sum(parsenums(_))

print('Общее количество занятий:')
for key in subjects.keys():
    print(f'{key:.<20}....{subjects[key]:.>4}')

# for subj in subj_splitted:
#     for item in subj:
#         for wtype in types:
#             if wtype in item:
#                 item = item.replace(wtype, '')
#                 subj_splitted[subj_splitted.index(subj)] = int(item) if item.isnumeric() else 0
#     subjects[subjects_lst[subj_splitted.index(subj)]] = sum(subj)
