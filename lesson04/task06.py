# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении
# числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие,
# при котором повторение элементов списка будет прекращено.
import itertools as it
import random as r

# а)
seed, count_nums = r.randint(1,5), []

for i in it.count(start=5, step=seed):
    count_nums.append(i)
    if i >= 20:
        break
print(f'RandInt = {seed},', count_nums)

# б) используем ранее сгенерированный список
tries = r.randint(len(count_nums), len(count_nums)*5)
counter = 0
cycled_lst = []
for elem in it.cycle(count_nums):
    if counter >= tries:
        break
    cycled_lst.append(elem)
    counter += 1
print('\n', cycled_lst)
