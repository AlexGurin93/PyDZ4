# 1) Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

number = int(input('Введите размер списка: '))
sum_of_el = 0
new_list = []
for i in range(number):
    list1 = int(input(f'Введите число   {i + 1} : '))
    new_list.append(list1)
    if i % 2 == 1:
        sum_of_el += new_list[i]
print(new_list)
print(sum_of_el)
