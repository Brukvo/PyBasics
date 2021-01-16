"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
выводить ее на экран.
"""
import random as r

raw_nums = None
rand_list = [str(r.randint(1, 10000)) for _ in range(r.randint(20, 50))]
with open('random_numbers.txt', 'a') as file_write:
    file_write.write(' '.join(rand_list))

with open('random_numbers.txt', 'r') as file_read:
    raw_nums = file_read.read()

numbers = [int(num) for num in raw_nums.split()]
print(f'Сумма чисел в файле: {sum(numbers)}')
