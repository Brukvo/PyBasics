# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
user_input = input('Введите несколько слов, разделённых пробелами: ')
words = user_input.split(' ')

for i, word in enumerate(words, start=1):
    print(f'{i:0>2}. {word[:10]}')