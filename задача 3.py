# Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию, методом сортировки выбором.
import random

rand_list = []
n = 30
for i in range(n):
    rand_list.append(random.randint(0, 10))
print(f'Изначальный список: {rand_list} ')
def sort(alist):
    for i in range(0, len(alist) - 1):
        smallest = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[smallest]:
                smallest = j
        alist[i], alist[smallest] = alist[smallest], alist[i]


alist = rand_list
alist = [int(x) for x in alist]
sort(alist)
print('Отсортированный: ', end='')
print(alist)
# Очень надеюсь научиться сортировать неповторяющиеся элементы