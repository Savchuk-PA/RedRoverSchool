# Имеется список items = [1.2, 3, None, 100, {'info': 'bla-bla'}, 44, 'Hi!', 99, 44.32, None]
# Составьте новый список numbers, который содержит только целые числа (int) и вещественные числа (float) из списка items
# Выведите на экран сумму чисел в numbers.
#
# Ответ: 291.52

items = [1.2, 3, None, 100, {"info": "bla-bla"}, 44, "Hi!", 99, 44.32, None]
num_items = [item for item in items if isinstance(item, float) or isinstance(item, int)]
print(sum(num_items))
