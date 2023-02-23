# Найти произведение всех целых чисел от 5 до 20 включительно.

# mult = 1
# for i in range(5,21):
#     mult += i
# print(mult)

# n = int(input("enter count of cow:"))
# for cow in range(1, cows +1):
#     if cow  % 10 == 1 and cow % 100 != 11:
#         print(f"{cow} корова")

# 11.	Даны натуральные числа n, m.
# Получить все числа меньше m взаимно простые с n.
# взаимно простые числа - числа с nod = 1 (4,5) (12,29) (15,16)
# n,m = map(int,input("enter n,m").split())
# for numb in range(2,m+1):
#     temp_numb = numb
#     temp_n = n
#     while temp_numb != 0 and temp_n != 0:
#         if temp_numb > temp_n:
#             temp_numb %= temp_n
#         else:
#             temp_n %= temp_numb
#     if temp_n + temp_numb == 1:
#         print(f"{numb} is simpe with {n}")

# tuple(кортежи) содержит типы данных в стогом порядке. не изменяем(как строки)
# unmutable
#     -5   -4   -3   -2   -1
#      0    1    2    3    4
# tup = ('hello', 54, True, 5.23, 54)
# его можно перебрать, применить к двум элементам count(считает количество вхождений в строку)
# второй метод поиск по индексу чисел
# перебор по элементам

# if 54 in tup:
#     print('in')
# else:
#     print('not')
# print(id(tup))
# tup2 = (1,4,5)
# tup += tup2
# print(tup)
# print(id(tup))

# кортеж применяется для хранения данных и требуем меньше памяти для хранения
# s = 'hello'
# tup = tuple(s.split())
# print(tup)

# tup = (5, 6, 1, 10, 18, 5, 2)
# # найти максимальный элемент
# max_el = tup[0]
# for elem in tup:
#     if elem > max_el:
#         max_el = elem
#     print(max_el)

# list (списки) mutable(изменяемые)
#       0   1      2     3     4       5
# lst = [5,2.42, 'hello', True, (6, 1, 2),[5, 2, 9]]
# tup = (5,2.42,'hello',True,(6,1,2),[5, 2, 9])
# print(lst.__sizeof__()) # sizeof показывает размер списка
# print(tup.__sizeof__())

# #       0   1      2     3        4       5
# lst = [5,2.42, 'hello', True, (6, 1, 2),[5, 2, 9]]
# print(id(lst))
#
# lst += [5, 2, 6]
# print(id(lst))

#       0   1      2     3        4       5
# lst = [5,2.42, 'hello', True, (6, 1, 2),[5, 2, 9]]
#
# lst += 'hello'
# print(lst)

#     0   1      2     3        4       5
# lst = [5,2.42, 'hello', True, (6, 1, 2),[5, 2, 9]]
#
# lst.append([5.23,4,2]) # добавлять в конец
# print(lst)

# #    0   1      2     3        4       5
# lst = [5,2.42, 'hello', True, (6, 1, 2),[5, 2, 9]]
#
# lst.insert(10, 5) # добавлять
# print(lst)

# #      0   1  2     3        4       5         6
# lst = [5,2.42,5, 'hello', True, (6, 1, 2),[5, 2, 9]]
# while 5 in lst:
#     lst.remove(5) # удалить 5 в списке
# print(lst)

# #      0   1  2     3        4       5         6
# lst = [5,2.42,5, 'hello', True, (6, 1, 2),[5, 2, 9]]
# lst.pop(4) # удалить определенный элемент в списке
# print(lst)

# #      0   1  2     3        4       5         6
# lst = [5,2.42,5, 'hello', True, (6, 1, 2),[5, 2, 9]]
# if 15 in lst:
#     lst.remove(15) # удаление по значению

# #      0   1  2     3        4       5         6
# lst = [5,2.42,5, 'hello', True, (6, 1, 2),[5, 2, 9]]
# del lst[3:5] # удаляет от 3 до 5

#
# #      0   1  2     3        4       5         6
# lst = [5,2.42,5, 'hello', True, (6, 1, 2),[5, 2, 9]]
# lst.clear() # удаление всех элементов
# print(lst)

# #      0   1  2     3        4       5         6
# lst = [5,2.42,5, 'hello', True, (6, 1, 2),[5, 2, 9]]
# print(lst.index(5, 3, 6)) # находит первое вхождение элемента

# #      0   1  2     3        4       5         6
# lst = [5,2.42,5, 'hello', True, (6, 1, 2),[5, 2, 9]]
# lst.count(4) # находит количество элементов

# #      0   1  2     3        4       5         6
# lst = [5,2.42,5, 'hello', True, (6, 1, 2),[5, 2, 9]]
# lst.extend((["hello"])) # добавление в конец список(могут быть строки, кортеж или список) (число нельзя добавить)
# print(lst)


# #      0   1  2     3        4       5         6
# lst = [5,2.42,5, 'hello', True, (6, 1, 2),[5, 2, 9]]
# lst2 = lst.copy() копирует список и можно изменять во втором всё
# print(lst2)

# #     0   1  2     3        4       5         6
# lst = [5,2.42,5, 'hello', True, (6, 1, 2),[5, 2, 9]]
# lst2 = lst
# lst2.remove(5)
# print(lst2)

# #     0   1  2     3        4       5         6
# lst = [5,2.42,5, 'hello', True, (6, 1, 2),[5, 2, 9]]
# lst2 = lst.copy()
#
# lst2.remove(5)
# print(lst2)
# print(lst)

# s = "hello"
# lst = list([4,5,2]) # сами создаём кортеж, добавляем в список
# print(lst)

# lst = []
# n = int(input("enter count of elem"))
# for i in range(n):
#     elem = int(input('enter elem:'))
#     lst.append(elem)
# print(lst) # ввели какой-то элемент от руки в список

# list comprehension
#1 [что хотим добавить for из чего in итерабельный объект]
#2 [что хотим добавить for из чего in итерабельный объект if если условие верно]
#3 [что хотим добавить if условие верное else что хотим добавить]
# print("чётное" if 4 % 2 == 0 else "нечётное")
# print([numb.upper() for numb in "Hello"])
# print([numb**3 for numb in range(1,11)]) # выводим кубы чисел
# print([numb for numb in range(1,11) if numb**2 % 3 == 0]) # не работает
# print([numb for numb in range(1,11) if numb**2 % 3 == 0])
# print([symb for symb in range(1,11) if symb**2 % 3 == 0])
# print([numb if numb % 2 ==0 else numb**2 for numb in range(1,11)]) # добавление тернарной операции
# print([int(input()) for i in range(5)]) # вводим сами числа до 5
# print([int(i) for i in input().split()]) # вводим сколько хотим чисел
# s = "hello world i am Piter Parker"
# lst = s.split() # каждый элемент станет отдельным списком
# print(lst)

# s = "hello world i am Piter Parker"
# lst = s.split()
# lst = [elem for elem in lst if elem[0].islower()]
# s = " ".join(lst) # удаляем конец и делаем строку
# print(s)


















