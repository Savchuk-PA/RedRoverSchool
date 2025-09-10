# Сгенерируйте список numbers, состоящий из чисел в диапазоне от 0 до 100 включительно,
# которые делятся без остатка как на 2, так и на 3.
# Выведите список numbers на экран.

# способ 1

numbers = [_ for _ in range(101) if _ % 2 == 0 and _ % 3 == 0]
print(numbers)

# способ 2
numbers_2 = []
for _ in range(101):
    if _ % 2 == 0 and _ % 3 == 0:
        numbers_2.append(_)
print(numbers_2)
