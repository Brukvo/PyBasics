# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
# Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.

print([_ for _ in range(20,241) if not _ % 20 or not _ % 21])
