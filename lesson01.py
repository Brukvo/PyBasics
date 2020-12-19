"""
1. Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные,
выведите на экран.
"""

number = 10
oneline_string = "Hello world!"
another_string = 'Hello again!'
multiline_string = """
Hi There!
It's Python!
"""

print(f'{number:*<80}')
print(f'{oneline_string:_^80}')
print(f'{another_string:.>80}')
print(f'\n\n{"Многострочное выражение:":^80}\n{multiline_string:=^80}')

# user_string = input('Напишите что-нибудь: ')

# Не самый удачный вариант, скрипт может вылететь с ошибкой, если не будет цифр.
# user_int = int(input('Введите какое-нибудь ЦЕЛОЕ число: '))

user_checkint = input('Проверка, что Вы вводите только цифры: ')
# Можно использовать пару вариантов в качестве замены:
#     1. через встроенную в тип данных 'str' метод isnumeric():
if user_checkint.isnumeric():
    print('Да, Вы ввели только цифры.')
    checkint_1m = int(user_checkint)
else:
    print('В строке присутствовали другие символы, кроме цифр')

#     2. через блок try-except:
try:
    checkint_2m = int(user_checkint)
except ValueError:
    print('В введённой Вами строке присутствовали другие символы, кроме цифр.')
    
################################################################################

"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и
секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""

raw_time = int(input('Введите время в секундах: '))

secs, mins, hours = raw_time % 60, (raw_time // 60) % 60, raw_time // 3600

print(f'Время: {hours:0>2}:{mins:0>2}:{secs:0>2}')

################################################################################

'''
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''

raw_num = input('Введите число от 1 до 9: ')
num1, num2, num3 = int(raw_num), int(raw_num*2), int(raw_num*3)

print(f'Итоговая сумма: {num1} + {num2} + {num3} =', num1 + num2 + num3)

################################################################################

'''
4. Пользователь вводит целое положительное число. Найдите самую большую цифру
в числе. Для решения используйте цикл while и арифметические операции.
'''

raw_max_num = input('Введите целое положительное число: ')
i = 9

while i >= 0:
    if str(i) in raw_max_num:
        break
    elif raw_max_num == '':
        print('Извините, но нужно было хоть что-то ввести! Завершаем работу.')
    elif not raw_max_num.isnumeric():
        print("Вводится только целое число")
    elif int(raw_max_num) < 0:
        print('Нужно было ввести ПОЛОЖИТЕЛЬНОЕ целое число.')
    else:
        i -= 1

print(f'Максимальная цифра в Вашем числе {raw_max_num}: {i}')

################################################################################

'''
5. Запросите у пользователя значения выручки и издержек фирмы. Определите,
с каким финансовым результатом работает фирма (прибыль — выручка больше
издержек, или убыток — издержки больше выручки). Выведите соответствующее
сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
(соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы
и определите прибыль фирмы в расчете на одного сотрудника.
'''

income = int(input('Выручка фирмы (в у.е.): '))
expenses = int(input('Расходы фирмы (в у.е.): '))

if income > expenses:
    print('Выручка больше расходов.')
    royalty = income - expenses
    print(f'Рентабельность: {royalty / income:.2f}')
    quantity = int(input('Число сотрудников: '))
    print(f'На одного сотрудника приходится {royalty / quantity} у.е. прибыли.')
elif income == expenses:
    print('Работаете в ноль.')
else:
    print('Слишком много расходов.')
    
################################################################################

'''
6. Спортсмен занимается ежедневными пробежками. В первый день его результат
составил a километров. Каждый день спортсмен увеличивал результат на 10 %
относительно предыдущего. Требуется определить номер дня, на который общий
результат спортсмена составить не менее b километров. Программа должна принимать
значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:

1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
'''

start_km = int(input('Введите НАЧАЛЬНОЕ число километров в первый день: '))
final_km = int(input('Введите КОНЕЧНОЕ число километров: '))
kms = start_km
days = 1

while True:
    print(f'{days}-й день: {kms:.2f} км')
    if kms < final_km:
        kms += (kms / 10)
        days += 1
        continue
    else:
        break

print(f'На {days}-й день спортсмен достиг результата - не менее {final_km} км.')