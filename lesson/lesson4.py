# for number in range(12,-8,-1):
#     if number % 2 == 0:
#       print(number,end=" ")

# s = 'hello world'
# for symb in s:
#     print(symb)
# for ind in range(0,len(s):
#     print(ind, s[ind])

# цикл с условие

# while True - бесконечный цикл (при False в цикл не войдёт)
# break - досрочно прирывает цикл

# count_dish = 0
# while True == 'да': # True/False
#
#     answer = input("Введите есть ли посуда(да/нет):")
#     if answer == 'нет':
#         break
#     print('берём тарелку, моем, сушим')
#     count_dish += 1
#
# print('мы вымыли ',count_dish,'посуды')
# if count_dish != 0:
#     print('отдыхаем после мытья посуды')
# else:
#     print('кто-то помыл посуду?')

# вывести все числа от 1 до n с помощью цикла while

# n = int(input('Введите конечное число'))
# begin = 1
# while begin <= n:
#     print(begin,end=' ')
#     begin += 1
# print('\nцикл завершён')
# for i in range(begin, n + 1):
#     print(i,end=' ')

# статистика рождаемости

# count_babies = 0
# count_days = 0
# while True:
#     stat = int(input("введите количество новорожденных:"))
#     if stat == 0:
#         break
#     count_babies += stat
#     count_days += 1
#
# print('колличество новорождённых:', count_babies)
# print('количество дней работы:', count_days)

# дано число, вывести все его цифры

# number = int(input("введите число")[::-1])
# number = int(number)
# while number != 0:
#     n = number % 10
#     print(n)
#     number = number // 10

# дано число - вывести все его цифры

# ниже идёт сложение чисел
# number = input("введите число:") # 532532523
# summa = 0
# for n in "532532523":
#     summa += int(n)
#     print(summa)

# найти нод двух чисел. Наибольший общий делитель

# numb, numb2 = map(int, input().split())
# numb = abs(numb)
# numb2 = abs(numb2)
# numbers = 1 # 1 .. numb, numb2
# nod = 1
# while True:
#     if numb % numbers == 0 and numb2 % numbers == 0: # показывает деление без остатка
#         nod = numbers
#     numbers += 1
#     if numbers > numb or numbers > numb2:
#         print('nod is', nod)
#         break

# строки, задачи по строкам (можно перебрать по циклам, строка не изменяема)

# s = 'hello'
# print(id(s))
# s = s.upper()
# print(id(s))
# s = s.lower()
# print(id(s))
# print(s)

#    012345678910
# len(s) = 11

# s = 'hello world'
# temp = ""
# for ind in range(len(s)):
#     if ind == len(s)-2:
#         temp += s[ind].upper()
#         continue # пропускает все команды, которые идут после него
#     temp += s[ind]
# print(temp)
# in - в
# not in - не в

# print('o' not in 'hell')
# s = 'hello world'
# gL = 'aeyuioAEYUIO'
# temp = ""
# print(len(s))
# for ind in range(len(s)): # 0 1 2 3 .. 10
#     print(s[ind])
#     if s[ind] in gL:
#         temp += s[ind]
# print(temp)

# text = "dog   cat frog   mouse "
# temp = ""
# for ind in range(len(text)):
#     if text[ind] != ' ':
#         temp += text[ind]
#     elif temp: # если строка существует(она пустая)
#         print(temp)
#         temp = ""

# В каких словах слово "о" встречается

# text = "dog   cat frog   mouse "
# temp = ""
# letter = 'o'
# count = 0
# for ind in range(len(text)):
#     if text[ind] != ' ':
#         temp += text[ind]
#     elif temp: # если строка существует(она пустая)
#         if letter in temp:
#          print(temp)
#         count += 1
#         temp = ""
# print(count)

# name = 'John'
# age = 45
# print('name:', name, 'age:',age)
# # форматированные стркоки
# print("name: {} age: {}".format(name,age)) # вот этот метод будем использвать ближайшее время
# # f-string f-натации

# print(f"name: {name.upper()} age: {age - 3}")
# # вывод строки через спецификаторы
# # %s - string (для строк)
# # %f - float (вещественные числа с точкой плавающей)
# # %d - int (для числа)
# print("name: %s age: %d" % (name,age))

# number = int(input("enter number:"))
# # numb 1 .. 11
# for numb in range(1, number, +1):
#     if number % numb == 0:
#         count += 1
#         print(numb)
# if count == 2:
#     print('простое')
# else:
#     print('не простое.')
#
#







