# 4. Представлен список чисел. Определить элементы списка, не имеющие
# повторений. Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]
import random as r

random_numbers = [r.randint(1,1000) for _ in range(100)]
print(f'Исходный набор чисел (длина - {len(random_numbers)}):\n{random_numbers}\n')

numbers = [_ for _ in random_numbers if random_numbers.count(_) == 1]
print(f'Итоговый набор чисел (длина - {len(numbers)}):\n{numbers}')
