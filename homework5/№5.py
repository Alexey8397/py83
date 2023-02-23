# 1. Дан кортеж. Вывести все его совершенные числа. (6,2,7,8)
# 6 = 1 + 2 + 3
# 28 = 1 + 2 +4 + 7 +14

# a = [6,2,7,8,11,22,12,28]
# for i in a:
#     b = 0
#     for j in range(1, i):
#         if i % j == 0:
#             b += j
#     if i == b:
#         print(i)

# 2. Дан кортеж. Найти разность между его максимальным и минимальный элементом.

# tup = (6, 3, 12, 20, 4)
# max = 0
# min = tup[0]
# for i in tup:
#     if i > max:
#         max = i
#     if i < min:
#         min = i
# print(max)
# print(min)
# print(max - min)

# max_number = max(tup)
# min_number = min(tup)
# print("Максимальное число:", max_number)
# print("Минимальное число:", min_number)
# max_number -= min_number
# print("Разносить между max и min:", max_number)

# 3. Дан кортеж. Написать программу, определяющую сколько раз менялся знак в кортеже. (5,2,-2,7,-8,-9,1) 4 раза

# tup = (5,2,-2,7,-8,-9,1)
# counter = 0
# el_elem = tup[0] < 0
# for el in range(1, len(tup[1:]) + 1):
#     if (tup[el] < 0) != el_elem:
#         counter += 1
#     el_elem = tup[el] < 0
# print(counter)

# проще способ решения

# tup = (5,2,-2,7,-8,-9,1)
# count = 0
# for ind in range(len(tup)-1):
#     if (tup[ind] > 0 and tup[ind + 1] < 0) or (tup[ind] < 0 and tup[ind + 1] > 0):
#         count += 1
# print(count)


# 4. Дан кортеж. Вывести на экран все простые числа в данном кортеже.

# tup = (2, 5, 11, 12, 13, 15, 21, 27, 29, 31, 32)
# n = int(input("Введите начало диапазона для поиска простых чисел: "))
# m = int(input("Введите конец диапазона для поиска простых чисел: "))
# for num in range(n, m):
#     count = 0
#     delitel = 2
#     while delitel < num:
#         if num % delitel == 0:
#             count += 1
#         delitel += 1
#     if count == 0:
#         print(f'{num} простое число')

# 5.	*Дан кортеж. Найти максимальную по длине монотонную последовательность
# ( убывающую или возрастающую) чисел.
# (5,2,6,8,9,7,5,7,8)

# tup = (5, 2, 6, 8, 9, 7, 5, 7, 8)
# count = 1
# max_count = 0
# for ind in range(len(tup)-1):
#     if tup[ind] < tup[ind+1]:
#         count += 1
#     else:
#         if count > max_count:
#             max_count = count
#         count = 1
# print(max_count)

# задачи на списки

# 7. Выведите все четные элементы списка.
# При этом используйте цикл for, перебирающий элементы списка, а не их индексы!

# s = (input("Введите числа:"))
# a = [int(s) for s in s.split()]
# for i in a:
#     if int(i) % 2 == 0:
#      print(i, end=' ')

# 8. Задано два списка.
# Найти наименьшие среди элементов первого списка, которые не входят во второй список.

# lst1 = [1, 2, 5, 7, 8, 3, 8, 10]
# lst2 = [1, 2, 8, 4, 2, 10]
# lst3 = []
# for elem in lst1:
#     if elem not in lst2:
#         lst3.append(elem)
# if len(lst3) == 0: # существует ли список
#     print("no data") #
# else:
#     print(min(lst3))

# 10. Дан список положительных целых чисел .
# Вставить после каждого чётного числа его перевёртыш.
# 18 81, 42 24, 8 8, 122 221

# lst = [6, 2, 8, 9, 10, 9998, 15, 24]
# # ind = 0
# # while ind < len(lst):
# #     if lst[ind] % 2 == 0:
# #         temp = str(lst[ind])[::-1]
# #         lst.insert(ind+1, int(temp))
# #         ind += 1
# #
# #     ind += 1
# # print(lst)

# 11.	Дан список .
# Вычислить сколько раз в нем встречается каждый элемент,
# не используя сортировки.
# [5,2,4,5,1,2] 1 – 1 2 – 2 4 – 1 5 - 2

# lst = [5, 2, 6, 6, 6, 2, 1, 1, 5, 2, 8]
# for ind in range(len(lst)):
# if lst[ind] not in lst[:ind]: # через срез убрать повторяющиеся
# if lst.index(lst[ind]) == ind: # нахождение элемента через первое вхождение
#             print(f"{lst[ind]} - {lst.count(lst[ind])}")


